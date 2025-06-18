import os
import pandas as pd
import shutil
from app import create_app
from app.extensions import db
from app.models import Building
from dotenv import load_dotenv

#Inicijalizacija aplikacije
load_dotenv()
app = create_app()
app.app_context().push()

#Putanje ka folderima
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STAGING_DIR = os.path.join(BASE_DIR, "data_import", "staging")
PROCESSED_DIR = os.path.join(BASE_DIR, "data_import", "processed")
ERRORED_DIR = os.path.join(BASE_DIR, "data_import", "errored")

USD_TO_EUR = 0.92
ACRE_TO_M2 = 4047
SQFT_TO_M2 = 0.092903

def process_csv_file(file_path):
    inserted = 0
    try:
        df = pd.read_csv(file_path)
        total = len(df)
        print(f"Ukupno redova: {total}")

        for index, row in df.iterrows():
            if str(row.get('status')).lower() != 'for_sale':
                continue

            # Proveri da li su ključna polja prisutna
            required_fields = ['price', 'bed', 'bath', 'house_size']
            if any(pd.isna(row.get(field)) for field in required_fields):
                continue

            try:
                # Konverzije
                price = float(row['price']) * USD_TO_EUR
                rooms = int(float(row['bed']))
                bathrooms = int(float(row['bath']))
                land_area = float(row.get('acre_lot', 0)) * ACRE_TO_M2
                square_footage = float(row.get('house_size', 0)) * SQFT_TO_M2

                # Dodaj nekretninu
                new_property = Building(
                    square_footage=square_footage,
                    rooms=rooms,
                    bathrooms=bathrooms,
                    price=price,
                    parking=False,
                    registration=True,
                    construction_year=None,
                    land_area=land_area,
                    estate_type_id=1,   # Zameni ako imaš druge ID-je
                    offer_id=1,
                    city_part_id=707
                )

                db.session.add(new_property)
                inserted += 1

            except Exception as e:
                continue  # preskoči red ako ne uspe

        if inserted > 0:
            db.session.commit()
            print(f"Ubaceno {inserted} redova.")
            return True
        else:
            print("Nema validnih redova.")
            return False

    except Exception as e:
        print(f"Greška pri čitanju fajla: {e}")
        db.session.rollback()
        return False

def run_import():
    for filename in os.listdir(STAGING_DIR):
        if filename.endswith(".csv"):
            full_path = os.path.join(STAGING_DIR, filename)
            print(f"\n Obrađujem fajl: {filename}")

            success = process_csv_file(full_path)

            if success:
                shutil.move(full_path, os.path.join(PROCESSED_DIR, filename))
                print("Premesteno u processed/")
            else:
                shutil.move(full_path, os.path.join(ERRORED_DIR, filename))
                print("Premesteno u errored/")

if __name__ == "__main__":
    run_import()



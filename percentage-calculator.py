import os

def count_classes_by_starting_number(folder_path):
    class_counts = {}  # Sınıfların sayısını tutacak bir sözlük oluşturuyoruz
    starting_number_mapping = {"0": "mug", "1": "goblet", "2": "can", "3": "bottle"}

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):  # Sadece .txt uzantılı dosyaları işleme alıyoruz
            file_path = os.path.join(folder_path, file_name)

            with open(file_path, 'r') as file:
                lines= file.readlines() #tüm satırları liste olarak alır

                for line in lines:
                    try:
                        starting_number = int(line.split()[0])  # İlk sayıyı alıyoruz

                    except ValueError:
                        starting_number = None

                    if starting_number is not None:
                        mapped_name = starting_number_mapping.get(str(starting_number))
                        if mapped_name is not None:
                            if mapped_name in class_counts:
                                class_counts[mapped_name] += 1
                            else:
                                class_counts[mapped_name] = 1

    return class_counts

# Veri setinin bulunduğu klasörün yolunu belirleyin
folder_path = "C:\\Users\\senayazici\\Desktop\\saatteknoloji\\alcoholv2_p2"

# Sınıf sayılarını hesaplayıp dönen sözlüğü alıyoruz
class_counts = count_classes_by_starting_number(folder_path)

total_classes = sum(class_counts.values())

# Başlangıç numarasına göre sınıf sayılarını ve yüzdelerini ekrana yazdırıyoruz
if class_counts:
    for starting_number, count in class_counts.items():
        percentage = (count / total_classes) * 100
        print(f"{starting_number} için {count} adet sınıf bulunuyor. Yüzde: {percentage:.2f}%")
else:
    print("Hiç veri bulunamadı.")

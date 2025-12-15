# Rancang-Bangun-Sistem-Daemon-Layanan-Otomatis-Di-Linux-
Adanya repo ini, yaitu untuk memenuhi tugas akhir mata kuliah sistem operasi.

## Fitur
- Berjalan otomatis saat boot
- Menulis log ke /var/log/mydaemon.log
- Modular: mudah dikembangkan

## Cara Instalasi
```bash
git clone -b master https://github.com/username/Proyek5-so
cd Proyek5-so

sudo cp service/mydaemon.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable mydaemon
sudo systemctl start mydaemon
```

## Link vidio demonstrasi instalasi
```
https://drive.google.com/drive/folders/1vRtM8tRFQED4ubI8ytocevUDLrYWHs8S?usp=sharing
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anggotatiminjection(models.Model):
    nama_lengkap = models.CharField(max_length=191)
    id_team = models.ForeignKey('Injection', models.DO_NOTHING, db_column='id_team')
    email = models.CharField(max_length=191)
    nim = models.CharField(max_length=191)
    nomor_telepon = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'AnggotaTimInjection'

    def __str__(self):
        return str(self.nama_lengkap) + " | " + str(self.email) + " | " + str(self.nim) + " | " + str(self.nomor_telepon)

class Dummytable(models.Model):
    nama = models.CharField(db_column='Nama', max_length=48)  # Field name made lowercase.
    umur = models.IntegerField(db_column='Umur')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=48)  # Field name made lowercase.
    kota = models.CharField(db_column='Kota', max_length=48)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DummyTable'

    

class Fotografi(models.Model):
    link_bukti_pembayaran = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    nama_lengkap = models.CharField(max_length=191)
    nomor_telepon = models.CharField(max_length=191)
    asal_sekolah = models.CharField(max_length=191)
    deskripsi_karya = models.CharField(max_length=191)
    domisili = models.CharField(max_length=191)
    judul_karya = models.CharField(max_length=191)
    link_bukti_follow = models.CharField(max_length=191)
    link_dokumen_keaslian = models.CharField(max_length=191)
    link_foto_karya = models.CharField(max_length=191)
    link_post_instagram = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'Fotografi'


class Injection(models.Model):
    nama_tim = models.CharField(unique=True, max_length=191)
    asal_sekolah = models.CharField(max_length=191)
    type = models.ForeignKey('Teamtype', models.DO_NOTHING, db_column='type')
    nama_pembimbing = models.CharField(max_length=191)
    no_telp_pembimbing = models.CharField(max_length=191)
    link_berkas_bukti = models.CharField(max_length=191)
    link_berkas_abstrak = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'Injection'

    def __str__(self):
        return str(self.nama_tim) + " | " + str(self.asal_sekolah) + " | " + str(self.nama_pembimbing) + " | " + str(self.no_telp_pembimbing) + " | " + str(self.link_berkas_bukti) + " | " + str(self.link_berkas_abstrak)

class Teamtype(models.Model):
    name = models.CharField(unique=True, max_length=191)

    class Meta:
        managed = False
        db_table = 'TeamType'


class User(models.Model):
    email = models.CharField(unique=True, max_length=191)
    namalengkap = models.CharField(max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'User'


class Verifikasi(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Verifikasi'


class PrismaMigrations(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    checksum = models.CharField(max_length=64)
    finished_at = models.DateTimeField(blank=True, null=True)
    migration_name = models.CharField(max_length=255)
    logs = models.TextField(blank=True, null=True)
    rolled_back_at = models.DateTimeField(blank=True, null=True)
    started_at = models.DateTimeField()
    applied_steps_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = '_prisma_migrations'

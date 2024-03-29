# Generated by Django 4.2.3 on 2024-02-06 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import products.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=512, unique=True, verbose_name="наименование")),
                ("description", models.TextField(blank=True, verbose_name="описание")),
                ("is_active", models.BooleanField(default=True)),
                ("sort_index", models.CharField(blank=True, verbose_name="индекс сортировки")),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="products.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Detail",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=512, verbose_name="наименование")),
            ],
            options={
                "verbose_name": "Характеристика",
                "verbose_name_plural": "Характеристики",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=512, verbose_name="наименование")),
                ("description", models.TextField(blank=True, verbose_name="описание")),
                ("date_of_publication", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "category",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="products.category"),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="ProductImport",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("file", models.FileField(upload_to="import/")),
            ],
            options={
                "verbose_name": "Импорт продукта",
                "verbose_name_plural": "Импорт продуктов",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField(blank=True, max_length=3000, verbose_name="Отзыв")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="products.product",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ProductsViews",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products_views",
                        to="products.product",
                        verbose_name="Продукт",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products_views",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "История просмотра",
                "verbose_name_plural": "История просмотров",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "image",
                    models.ImageField(
                        default=1, upload_to=products.models.product_image_directory_path, verbose_name="изображение"
                    ),
                ),
                ("sort_image", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_images",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фотография продукта",
                "verbose_name_plural": "Фотографии продуктов",
            },
        ),
        migrations.CreateModel(
            name="ProductDetail",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("value", models.CharField(max_length=128, verbose_name="значение")),
                (
                    "detail",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.detail",
                        verbose_name="характеристика",
                    ),
                ),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="products.product")),
            ],
            options={
                "verbose_name": "Характеристика продукта",
                "verbose_name_plural": "Характеристики продукта",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="details",
            field=models.ManyToManyField(
                through="products.ProductDetail", to="products.detail", verbose_name="характеристики"
            ),
        ),
        migrations.CreateModel(
            name="ComparisonList",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("anonymous_user", models.BooleanField(default=False)),
                (
                    "products",
                    models.ManyToManyField(blank=True, related_name="comparison_list", to="products.product"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "verbose_name": "Список сравнения",
                "verbose_name_plural": "Списки сравнения",
            },
        ),
        migrations.CreateModel(
            name="Banner",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "image",
                    models.ImageField(
                        upload_to=products.models.banner_preview_directory_path, verbose_name="изображение"
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="banners", to="products.product"
                    ),
                ),
            ],
            options={
                "verbose_name": "Баннер",
                "verbose_name_plural": "Баннеры",
            },
        ),
        migrations.AddConstraint(
            model_name="productdetail",
            constraint=models.UniqueConstraint(
                models.F("product"), models.F("detail"), name="unique_detail_for_product"
            ),
        ),
    ]

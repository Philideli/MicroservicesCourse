CREATE TABLE IF NOT EXISTS "flower" (
	"id"	SERIAL PRIMARY KEY,
	"name"	TEXT,
	"color"	TEXT,
	"climate"	TEXT,
	"price"	INT,
	"image"	TEXT
);

INSERT INTO flower VALUES
(1,'Rose','Red, pink, white','Temperate',15,'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Red_rose_with_black_background.jpg/640px-Red_rose_with_black_background.jpg'),
(2,'Tulip','Red, pink, white','Temperate',12,'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Tulipa_suaveolens_floriade_to_Canberra.jpg/640px-Tulipa_suaveolens_floriade_to_Canberra.jpg'),
(3,'Daisy','White, yellow','Temperate',8,'https://upload.wikimedia.org/wikipedia/commons/c/ce/Daisy_G%C3%A4nsebl%C3%BCmchen_Bellis_perennis_01.jpg'),
(4,'Sunflower','Yellow, orange','Temperate to tropical',7,'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Sonnenblume_Helianthus_1.JPG/640px-Sonnenblume_Helianthus_1.JPG'),
(5,'Orchid','Purple, pink, white','Tropical',45,'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Orchid_4035.jpg/640px-Orchid_4035.jpg'),
(6,'Jasmine','White, yellow','Tropical',37,'https://upload.wikimedia.org/wikipedia/commons/e/e5/Jasmine_flower.jpg'),
(7,'Lavender','Purple','Temperate',14,'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Single_lavender_flower02.jpg/640px-Single_lavender_flower02.jpg'),
(8,'Marigold','Orange, yellow','Tropical to temperate',13,'https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Tagetes-Marigold-Flower_04.jpg/640px-Tagetes-Marigold-Flower_04.jpg'),
(9,'Chrysanthemum','Red, white, yellow','Temperate',35,'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Chrysanthemum_sp.jpg/640px-Chrysanthemum_sp.jpg'),
(10,'Daffodil','Yellow, white','Temperate',43,'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Narcissus_sp._%28daffodil%29_%28Newark%2C_Ohio%2C_USA%29_18_%2816741215724%29.jpg/640px-Narcissus_sp._%28daffodil%29_%28Newark%2C_Ohio%2C_USA%29_18_%2816741215724%29.jpg'),
(11,'Freesia','Red, pink, white','Temperate',62,'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Flowers_February_2009-1.jpg/640px-Flowers_February_2009-1.jpg'),
(12,'Iris','Purple, blue, white','Temperate to tropical',48,'https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Iris_versicolor_4.jpg/640px-Iris_versicolor_4.jpg'),
(13,'Lily','White, yellow, pink','Temperate to tropical',75,'https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/LiliumBulbiferumCroceumBologna.jpg/800px-LiliumBulbiferumCroceumBologna.jpg?20070620075120'),
(14,'Peony','Red, pink, white','Temperate',60,'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Paeonia_suffruticosa_Yatsuka_JdP.jpg/640px-Paeonia_suffruticosa_Yatsuka_JdP.jpg'),
(15,'Gardenia','White, yellow','Tropical',33,'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Starr-200721-7837-Gardenia_augusta-flower-Hawea_Pl_Olinda-Maui_%2850335519438%29.jpg/640px-Starr-200721-7837-Gardenia_augusta-flower-Hawea_Pl_Olinda-Maui_%2850335519438%29.jpg'),
(16,'Gladiolus','Red, pink, white','Tropical',27,'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Gladiolus_illyricus.JPG/640px-Gladiolus_illyricus.JPG'),
(17,'Hyacinth','Blue, pink, white','Temperate',57,'https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Blue_Hyacinth.jpg/640px-Blue_Hyacinth.jpg'),
(18,'Lilac','Purple, pink, white','Temperate',18,'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Lilac_Flower%26Leaves%2C_SC%2C_Vic%2C_13.10.2007.jpg/640px-Lilac_Flower%26Leaves%2C_SC%2C_Vic%2C_13.10.2007.jpg'),
(19,'Narcissus','Yellow, white','Temperate',20,'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Narcissus_R01.jpg/640px-Narcissus_R01.jpg'),
(20,'Poppy','Red, pink, white','Temperate',25,'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Pink_Poppy3.jpg/800px-Pink_Poppy3.jpg?20200721232052')
-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           PostgreSQL 16.3, compiled by Visual C++ build 1939, 64-bit
-- OS do Servidor:               
-- HeidiSQL Versão:              12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Copiando estrutura para tabela public.user
CREATE TABLE IF NOT EXISTS "user" (
	"id" SERIAL NOT NULL,
	"username" VARCHAR(150) NOT NULL,
	"password" VARCHAR(150) NOT NULL,
	"role" VARCHAR(50) NOT NULL,
	PRIMARY KEY ("id"),
	UNIQUE "User_username_key" ("username")
);

-- Copiando dados para a tabela public.user: 2 rows
/*!40000 ALTER TABLE "user" DISABLE KEYS */;
INSERT INTO "user" ("id", "username", "password", "role") VALUES
	(1, 'user', 'pbkdf2:sha256:600000$1UsE79L56mlb4jFn$0280071c36d52a42a265a2dbf58eaceb5ff82c72c68e2027952dcd3b6d72bdab', 'user'),
	(2, 'admin', 'pbkdf2:sha256:600000$hYgbsvaPgoPLoA8J$9df6495078caceaa2245d0c10be482dc5fcf2b02c493c1db38818d12c48dcc49', 'admin');
/*!40000 ALTER TABLE "user" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

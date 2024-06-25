-- MySQL dump 10.13  Distrib 8.3.0, for macos14.2 (arm64)
--
-- Host: localhost    Database: testsigma_opensource
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `addon_natural_text_action_parameters`
--

DROP TABLE IF EXISTS `addon_natural_text_action_parameters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addon_natural_text_action_parameters` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `addon_natural_text_action_id` bigint DEFAULT NULL,
  `parameter_type` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `reference` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `name` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `allowed_values` mediumtext COLLATE utf8mb3_unicode_ci,
  PRIMARY KEY (`id`),
  KEY `index_addon_natural_text_action_parameters_on_text_action_id` (`addon_natural_text_action_id`),
  CONSTRAINT `fk_addon_natural_text_action_id_to_addon_natural_text_actions` FOREIGN KEY (`addon_natural_text_action_id`) REFERENCES `addon_natural_text_actions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `addon_natural_text_actions`
--

DROP TABLE IF EXISTS `addon_natural_text_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addon_natural_text_actions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `addon_id` bigint DEFAULT NULL,
  `fully_qualified_name` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `natural_text` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `workspace_type` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `deprecated` tinyint(1) DEFAULT '0',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `condition_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_addon_natural_text_actions_on_workspace_type` (`workspace_type`),
  KEY `index_addon_natural_text_actions_on_addon_id` (`addon_id`),
  CONSTRAINT `fk_addon_id_in_addon_natural_text_actions_to_addons` FOREIGN KEY (`addon_id`) REFERENCES `addons` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `addon_plugin_test_data_function_parameters`
--

DROP TABLE IF EXISTS `addon_plugin_test_data_function_parameters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addon_plugin_test_data_function_parameters` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_data_function_id` bigint DEFAULT NULL,
  `parameter_type` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `reference` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `name` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb3_unicode_ci NOT NULL,
  `created_by_id` bigint DEFAULT NULL,
  `updated_by_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_test_data_function_id_in_addon_test_data_function_params` (`test_data_function_id`),
  CONSTRAINT `fk_test_data_function_id_in_addon_test_data_function_params` FOREIGN KEY (`test_data_function_id`) REFERENCES `addon_plugin_test_data_functions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `addon_plugin_test_data_functions`
--

DROP TABLE IF EXISTS `addon_plugin_test_data_functions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addon_plugin_test_data_functions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `addon_id` bigint DEFAULT NULL,
  `fully_qualified_name` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `display_name` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8mb3_unicode_ci NOT NULL,
  `deprecated` tinyint DEFAULT '0',
  `created_by_id` bigint DEFAULT NULL,
  `updated_by_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_addon_id_in_addon_test_data_functions` (`addon_id`),
  CONSTRAINT `fk_addon_id_in_addon_test_data_functions` FOREIGN KEY (`addon_id`) REFERENCES `addons` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `addons`
--

DROP TABLE IF EXISTS `addons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `addons` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `version` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `external_unique_id` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `external_installed_version_unique_id` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `modified_hash` varchar(256) COLLATE utf8mb3_unicode_ci NOT NULL,
  `status` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_addons_on_status_and_external_unique_id` (`status`,`external_unique_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `adhoc_run_configurations`
--

DROP TABLE IF EXISTS `adhoc_run_configurations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adhoc_run_configurations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `config_name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `workspace_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `page_timeout` int DEFAULT NULL,
  `type` int DEFAULT NULL,
  `capture_screenshots` int DEFAULT NULL,
  `environment_id` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `element_timeout` int DEFAULT NULL,
  `desired_capabilities` text COLLATE utf8mb3_unicode_ci,
  `browser` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `agent_id` bigint DEFAULT NULL,
  `app_name` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `platform_os_version_id` bigint DEFAULT NULL,
  `platform_browser_version_id` bigint DEFAULT NULL,
  `platform_screen_resolution_id` bigint DEFAULT NULL,
  `platform_device_id` bigint DEFAULT NULL,
  `device_name` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `udid` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_package` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_activity` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_upload_id` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_url` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_bundle_id` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `device_id` bigint DEFAULT NULL,
  `app_path_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_adhoc_run_configurations_on_work_type_and_config_name` (`workspace_type`,`config_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `agent_devices`
--

DROP TABLE IF EXISTS `agent_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agent_devices` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `unique_id` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `agent_id` bigint NOT NULL,
  `product_model` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `os_version` varchar(10) COLLATE utf8mb3_unicode_ci NOT NULL,
  `os_name` varchar(50) COLLATE utf8mb3_unicode_ci NOT NULL,
  `api_level` varchar(10) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `abi` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `browser_list` text COLLATE utf8mb3_unicode_ci,
  `is_emulator` tinyint(1) DEFAULT '0',
  `is_online` tinyint(1) DEFAULT '0',
  `screen_width` int DEFAULT NULL,
  `screen_height` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_agent_devices_on_agent_id_and_unique_id` (`agent_id`,`unique_id`),
  CONSTRAINT `fk_agent_id_in_agent_devices_to_agents` FOREIGN KEY (`agent_id`) REFERENCES `agents` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `agents`
--

DROP TABLE IF EXISTS `agents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agents` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `unique_id` varchar(36) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `agent_version` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `browser_list` text COLLATE utf8mb3_unicode_ci,
  `upgrade_agent_jar` tinyint(1) DEFAULT '0',
  `upgrade_jre` tinyint(1) DEFAULT '0',
  `upgrade_android_tools` tinyint(1) DEFAULT '0',
  `upgrade_ios_tools` tinyint(1) DEFAULT '0',
  `upgrade_appium` tinyint(1) DEFAULT '0',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `host_name` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `os_version` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `ip_address` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `os_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `type` int DEFAULT '4',
  `title` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `imported_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_agents_on_title` (`title`),
  UNIQUE KEY `index_agents_on_unique_id` (`unique_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `attachments`
--

DROP TABLE IF EXISTS `attachments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attachments` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `entity` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `entity_id` bigint NOT NULL,
  `type` int NOT NULL DEFAULT '1',
  `path` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_attachments_on_entity_and_entity_id_and_name` (`entity`,`entity_id`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `backup_details`
--

DROP TABLE IF EXISTS `backup_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `backup_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `xml_name` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` int DEFAULT NULL,
  `message` varchar(2000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `is_test_case_enabled` tinyint(1) DEFAULT '0',
  `is_test_step_enabled` tinyint(1) DEFAULT '0',
  `is_rest_step_enabled` tinyint(1) DEFAULT '0',
  `is_upload_enabled` tinyint(1) DEFAULT '0',
  `is_test_case_priority_enabled` tinyint(1) DEFAULT '0',
  `is_test_case_type_enabled` tinyint(1) DEFAULT '0',
  `is_element_enabled` tinyint(1) DEFAULT '0',
  `is_element_screen_name_enabled` tinyint(1) DEFAULT '0',
  `is_test_data_enabled` tinyint(1) DEFAULT '0',
  `is_attachment_enabled` tinyint(1) DEFAULT '0',
  `is_agent_enabled` tinyint(1) DEFAULT '0',
  `is_test_plan_enabled` tinyint(1) DEFAULT '0',
  `is_test_device_enabled` tinyint(1) DEFAULT '0',
  `is_suites_enabled` tinyint(1) DEFAULT '0',
  `is_label_enabled` tinyint(1) DEFAULT '0',
  `workspace_version_id` bigint DEFAULT '0',
  `filter_id` bigint DEFAULT NULL,
  `entity_id` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `skip_entity_exists` bit(1) DEFAULT NULL,
  `action_type` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `affected_cases_list_path` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `chrome_extention_details`
--

DROP TABLE IF EXISTS `chrome_extention_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chrome_extention_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `exclude_attributes` json DEFAULT NULL,
  `exclude_classes` json DEFAULT NULL,
  `include_classes` json DEFAULT NULL,
  `include_attriutes` json DEFAULT NULL,
  `chrome_extention_details` json DEFAULT NULL,
  `userdefined_attributes` json DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `default_data_generator_files`
--

DROP TABLE IF EXISTS `default_data_generator_files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `default_data_generator_files` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `class_package` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `class_name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `display_name` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89105 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `default_data_generators`
--

DROP TABLE IF EXISTS `default_data_generators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `default_data_generators` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `file_id` bigint DEFAULT NULL,
  `function_name` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `display_name` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `arguments` json DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_file_id_to_default_data_generator_files` (`file_id`),
  CONSTRAINT `fk_file_id_to_default_data_generator_files` FOREIGN KEY (`file_id`) REFERENCES `default_data_generator_files` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=89123 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `element_screen_names`
--

DROP TABLE IF EXISTS `element_screen_names`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `element_screen_names` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `version_id` bigint NOT NULL,
  `copied_from` bigint DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_elements_screen_names_on_version_id_name` (`version_id`,`name`),
  CONSTRAINT `fk_version_id_in_element_screen_names_to_workspace_versions` FOREIGN KEY (`version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `elements`
--

DROP TABLE IF EXISTS `elements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elements` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `workspace_version_id` bigint DEFAULT NULL,
  `locator_value` varchar(2054) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `element_name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `element_type` int DEFAULT NULL,
  `create_type` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT 'CHROME',
  `locator_type` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `metadata` json DEFAULT NULL,
  `attributes` json DEFAULT NULL,
  `is_dynamic` bit(1) DEFAULT b'0',
  `imported_id` bigint DEFAULT NULL,
  `copied_from` bigint DEFAULT NULL,
  `screen_name_id` bigint NOT NULL,
  `is_duplicated` bit(1) DEFAULT b'0',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_elements_on_workspace_version_id_and_field_name` (`workspace_version_id`,`element_name`),
  KEY `index_elements_on_workspace_version_id` (`workspace_version_id`),
  KEY `fk_screen_name_id_in_elements_to_element_screen_names` (`screen_name_id`),
  CONSTRAINT `fk_screen_name_id_in_elements_to_element_screen_names` FOREIGN KEY (`screen_name_id`) REFERENCES `element_screen_names` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_workspace_version_id_in_elements_to_workspace_versions` FOREIGN KEY (`workspace_version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=665 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `entity_external_mappings`
--

DROP TABLE IF EXISTS `entity_external_mappings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entity_external_mappings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `entity_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `entity_id` bigint NOT NULL,
  `application_id` bigint NOT NULL,
  `external_id` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `misc` text COLLATE utf8mb3_unicode_ci,
  `push_failed` tinyint(1) DEFAULT NULL,
  `assets_push_failed` tinyint(1) DEFAULT NULL,
  `message` text COLLATE utf8mb3_unicode_ci,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_application_id` (`application_id`),
  CONSTRAINT `fk_application_id_to_integrations` FOREIGN KEY (`application_id`) REFERENCES `integrations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `environments`
--

DROP TABLE IF EXISTS `environments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `environments` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `parameters` text COLLATE utf8mb3_unicode_ci,
  `passwords` json DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_environments_on_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `external_import_nlp_mappings`
--

DROP TABLE IF EXISTS `external_import_nlp_mappings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `external_import_nlp_mappings` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `workspace_type` varchar(100) NOT NULL,
  `testsigma_nlp_id` int NOT NULL,
  `external_nlp_id` varchar(255) NOT NULL,
  `external_import_type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_workspace_type_external_nlp_id_external_import_type` (`workspace_type`,`external_nlp_id`,`external_import_type`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `flyway_schema_history`
--

DROP TABLE IF EXISTS `flyway_schema_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flyway_schema_history` (
  `installed_rank` int NOT NULL,
  `version` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `description` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `type` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  `script` varchar(1000) COLLATE utf8mb4_general_ci NOT NULL,
  `checksum` int DEFAULT NULL,
  `installed_by` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `installed_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `execution_time` int NOT NULL,
  `success` tinyint(1) NOT NULL,
  PRIMARY KEY (`installed_rank`),
  KEY `flyway_schema_history_s_idx` (`success`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `for_step_conditions`
--

DROP TABLE IF EXISTS `for_step_conditions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `for_step_conditions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `test_step_id` bigint NOT NULL,
  `test_data_profile_id` bigint DEFAULT NULL,
  `test_case_id` bigint NOT NULL,
  `iteration_type` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `left_param_type` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `left_param_value` text COLLATE utf8mb3_unicode_ci,
  `operator` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `right_param_type` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `right_param_value` text COLLATE utf8mb3_unicode_ci,
  `left_function_id` bigint DEFAULT NULL,
  `right_function_id` bigint DEFAULT NULL,
  `test_data` text COLLATE utf8mb3_unicode_ci,
  `left_data_map` json DEFAULT NULL,
  `right_data_map` json DEFAULT NULL,
  `copied_from` bigint DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `copied_overriding_from` bigint DEFAULT NULL,
  `type` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL DEFAULT 'ORIGINAL',
  PRIMARY KEY (`id`),
  UNIQUE KEY `for_step_conditions_fk_id` (`id`),
  KEY `for_step_conditions_fk_test_step_id` (`test_step_id`),
  KEY `for_step_test_case_id` (`test_case_id`),
  KEY `for_step_conditions_fk_test_data_id` (`test_data_profile_id`),
  CONSTRAINT `for_step_conditions_fk_test_data_id` FOREIGN KEY (`test_data_profile_id`) REFERENCES `test_data` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `for_step_conditions_fk_test_step_id` FOREIGN KEY (`test_step_id`) REFERENCES `test_steps` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `for_step_test_case_id` FOREIGN KEY (`test_case_id`) REFERENCES `test_cases` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `integrations`
--

DROP TABLE IF EXISTS `integrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `integrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `workspace_id` bigint NOT NULL,
  `url` varchar(1024) COLLATE utf8mb3_unicode_ci NOT NULL,
  `username` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `auth_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `token` varchar(1024) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `metadata` json DEFAULT NULL,
  `workspace` varchar(500) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `refresh_key_expires_at` timestamp NULL DEFAULT NULL,
  `access_key_type` varchar(500) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `access_key` text COLLATE utf8mb3_unicode_ci,
  `access_key_issued_at` timestamp NULL DEFAULT NULL,
  `access_key_expires_at` timestamp NULL DEFAULT NULL,
  `refresh_key` text COLLATE utf8mb3_unicode_ci,
  `refresh_key_issued_at` timestamp NULL DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_integrations_on_workspace` (`workspace`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `list_filters`
--

DROP TABLE IF EXISTS `list_filters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `list_filters` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `version_id` bigint DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `query_hash` text COLLATE utf8mb3_unicode_ci,
  `is_public` bit(1) DEFAULT b'0',
  `is_default` bit(1) DEFAULT b'0',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_list_filters_on_name_and_type_and_is_public` (`name`,`type`,`is_public`),
  KEY `fk_version_id_in_list_filters_to_workspace_versions` (`version_id`),
  CONSTRAINT `fk_version_id_in_list_filters_to_workspace_versions` FOREIGN KEY (`version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mobile_inspections`
--

DROP TABLE IF EXISTS `mobile_inspections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mobile_inspections` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `platform` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `agent_device_id` bigint DEFAULT NULL,
  `status` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `lab_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `platform_device_id` bigint DEFAULT NULL,
  `app_activity` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `bundle_id` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `upload_version_id` bigint DEFAULT NULL,
  `capabilities` json DEFAULT NULL,
  `cookies` json DEFAULT NULL,
  `session_id` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `application_package` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `application_path_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `started_at` datetime DEFAULT NULL,
  `finished_at` datetime DEFAULT NULL,
  `last_active_at` datetime DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_mobile_inspections_on_status_and_last_active_at` (`status`,`last_active_at`),
  KEY `index_mobile_inspections_on_status_and_lab_type` (`status`,`lab_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `natural_text_action_examples`
--

DROP TABLE IF EXISTS `natural_text_action_examples`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `natural_text_action_examples` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `natural_text_action_id` bigint DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `example` text COLLATE utf8mb3_unicode_ci,
  `workspace` text COLLATE utf8mb3_unicode_ci,
  `data` json DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_natural_text_action_examples_on_natural_text_action_id` (`natural_text_action_id`),
  CONSTRAINT `fk_natural_text_action_id_to_natural_text_actions` FOREIGN KEY (`natural_text_action_id`) REFERENCES `natural_text_actions` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=889 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `natural_text_actions`
--

DROP TABLE IF EXISTS `natural_text_actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `natural_text_actions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `workspace_type` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `natural_text` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `data` text COLLATE utf8mb3_unicode_ci,
  `display_name` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `snippet_class` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `action` text COLLATE utf8mb3_unicode_ci,
  `import_to_web` int DEFAULT NULL,
  `import_to_mobile_web` int DEFAULT NULL,
  `import_to_android_native` int DEFAULT NULL,
  `import_to_ios_native` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `allowed_values` mediumtext COLLATE utf8mb3_unicode_ci,
  `condition_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `loop_type` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40062 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `private_grid_nodes`
--

DROP TABLE IF EXISTS `private_grid_nodes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `private_grid_nodes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `node_name` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `browser_list` text COLLATE utf8mb3_unicode_ci,
  `grid_url` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provisioning_profile_devices`
--

DROP TABLE IF EXISTS `provisioning_profile_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provisioning_profile_devices` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `provisioning_profile_id` bigint NOT NULL,
  `agent_device_id` bigint DEFAULT NULL,
  `device_udid` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_profile_devices_on_device_udid_and_agent_device_id` (`device_udid`,`agent_device_id`),
  KEY `index_provisioning_profile_devices_on_agent_device_id` (`agent_device_id`),
  KEY `index_provisioning_profile_devices_on_provisioning_profile_id` (`provisioning_profile_id`),
  CONSTRAINT `fk_agent_device_id_to_agent_devices` FOREIGN KEY (`agent_device_id`) REFERENCES `agent_devices` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_provisioning_profile_id_to_provisioning_profiles` FOREIGN KEY (`provisioning_profile_id`) REFERENCES `provisioning_profiles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provisioning_profile_upload_versions`
--

DROP TABLE IF EXISTS `provisioning_profile_upload_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provisioning_profile_upload_versions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `provisioning_profile_id` bigint NOT NULL,
  `upload_version_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_provisioning_profile_upload_versions_upload_version_id` (`upload_version_id`),
  KEY `fk_provisioning_profile_uploads_provisioning_profile_id` (`provisioning_profile_id`),
  CONSTRAINT `fk_provisioning_profile_upload_versions_upload_version_id` FOREIGN KEY (`upload_version_id`) REFERENCES `upload_versions` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_provisioning_profile_uploads_provisioning_profile_id` FOREIGN KEY (`provisioning_profile_id`) REFERENCES `provisioning_profiles` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provisioning_profiles`
--

DROP TABLE IF EXISTS `provisioning_profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provisioning_profiles` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `team_id` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_provisioning_profiles_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rest_step_details`
--

DROP TABLE IF EXISTS `rest_step_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rest_step_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `step_id` bigint NOT NULL,
  `url` text COLLATE utf8mb3_unicode_ci NOT NULL,
  `method` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `request_headers` text COLLATE utf8mb3_unicode_ci,
  `payload` mediumtext COLLATE utf8mb3_unicode_ci,
  `status` varchar(2000) COLLATE utf8mb3_unicode_ci NOT NULL,
  `header_compare_type` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `response_headers` text COLLATE utf8mb3_unicode_ci,
  `response_compare_type` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `response` text COLLATE utf8mb3_unicode_ci,
  `store_metadata` bit(1) DEFAULT NULL,
  `expected_result_type` varchar(40) COLLATE utf8mb3_unicode_ci NOT NULL,
  `header_runtime_data` json DEFAULT NULL,
  `body_runtime_data` json DEFAULT NULL,
  `follow_redirects` bit(1) DEFAULT b'1',
  `authorization_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT 'NONE',
  `authorization_value` json DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_rest_step_details_on_step_id` (`step_id`),
  CONSTRAINT `fk_step_id_in_rest_step_details_to_test_steps` FOREIGN KEY (`step_id`) REFERENCES `test_steps` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `runtime_data`
--

DROP TABLE IF EXISTS `runtime_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `runtime_data` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_plan_run_id` bigint NOT NULL,
  `session_id` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `data` json DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_runtime_data_on_test_plan_run_id_and_session_id` (`test_plan_run_id`,`session_id`),
  CONSTRAINT `fk_test_plan_run_id_in_runtime_data_to_test_plan_runs` FOREIGN KEY (`test_plan_run_id`) REFERENCES `test_plan_results` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `schedule_test_plans`
--

DROP TABLE IF EXISTS `schedule_test_plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schedule_test_plans` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_plan_id` bigint NOT NULL,
  `name` varchar(125) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `comments` varchar(45) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `schedule_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `schedule_time` timestamp NULL DEFAULT NULL,
  `status` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `queue_status` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT 'IN_PROGRESS',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_schedule_test_plans_on_test_plan_id_and_status` (`test_plan_id`,`status`),
  CONSTRAINT `fk_test_plan_id_in_schedule_test_plans_to_test_plans` FOREIGN KEY (`test_plan_id`) REFERENCES `test_plans` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `servers`
--

DROP TABLE IF EXISTS `servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `server_uuid` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `consent` tinyint(1) NOT NULL DEFAULT '0',
  `consent_request_done` tinyint(1) NOT NULL DEFAULT '0',
  `onboarded` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_servers_on_server_uuid` (`server_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `storage_config`
--

DROP TABLE IF EXISTS `storage_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage_config` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `storage_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `aws_bucket_name` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `aws_region` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `aws_endpoint` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `aws_access_key` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `aws_secret_key` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `azure_blob_connection_string` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `azure_blob_container_name` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `on_premise_root_directory` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `suggestion_result_mapping`
--

DROP TABLE IF EXISTS `suggestion_result_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suggestion_result_mapping` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `step_result_id` bigint DEFAULT NULL,
  `suggestion_id` int DEFAULT NULL,
  `result` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `message` text COLLATE utf8mb3_unicode_ci,
  `meta_data` json DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tag_entity_mapping`
--

DROP TABLE IF EXISTS `tag_entity_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tag_entity_mapping` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tag_id` bigint DEFAULT NULL,
  `entity_id` bigint DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_tag_entity_mapping_on_tag_id_and_entity_id_and_type` (`tag_id`,`entity_id`,`type`),
  CONSTRAINT `fk_tag_id_in_tag_entity_mapping_to_tags` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(2000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `count` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_case_data_driven_results`
--

DROP TABLE IF EXISTS `test_case_data_driven_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_case_data_driven_results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_case_id` bigint DEFAULT NULL,
  `test_data_name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `test_data` text COLLATE utf8mb3_unicode_ci,
  `test_device_result_id` bigint DEFAULT NULL,
  `test_case_result_id` bigint DEFAULT NULL,
  `iteration_result_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_case_data_driven_results_on_test_case_id` (`test_case_id`),
  KEY `index_on_test_device_result_id_and_iteration_result_id` (`test_device_result_id`,`iteration_result_id`),
  KEY `fk_test_case_result_id_to_test_case_results` (`test_case_result_id`),
  CONSTRAINT `fk_test_case_result_id_to_test_case_results` FOREIGN KEY (`test_case_result_id`) REFERENCES `test_case_results` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_case_priorities`
--

DROP TABLE IF EXISTS `test_case_priorities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_case_priorities` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `display_name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `workspace_id` bigint NOT NULL,
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_test_case_priorities_on_name_and_workspace_id` (`name`,`workspace_id`),
  KEY `index_test_case_priorities_on_workspace_id` (`workspace_id`),
  CONSTRAINT `fk_workspace_id_in_test_case_priorities_to_workspaces` FOREIGN KEY (`workspace_id`) REFERENCES `workspaces` (`id`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_case_results`
--

DROP TABLE IF EXISTS `test_case_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_case_results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_case_id` bigint NOT NULL,
  `test_plan_result_id` bigint DEFAULT NULL,
  `test_device_result_id` bigint NOT NULL,
  `suite_id` bigint DEFAULT NULL,
  `iteration` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `result` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT 'STATUS_CREATED',
  `is_step_group` int DEFAULT NULL,
  `message` text COLLATE utf8mb3_unicode_ci,
  `start_time` timestamp NULL DEFAULT NULL,
  `end_time` timestamp NULL DEFAULT NULL,
  `duration` bigint DEFAULT NULL,
  `suite_result_id` bigint DEFAULT NULL,
  `parent_id` bigint DEFAULT NULL,
  `test_data_set_name` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `order_id` bigint DEFAULT NULL,
  `type` int DEFAULT NULL,
  `test_case_status` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `test_data_details` json DEFAULT NULL,
  `is_data_driven` bit(1) DEFAULT NULL,
  `test_data_id` bigint DEFAULT NULL,
  `test_case_details` json DEFAULT NULL,
  `started` bit(1) DEFAULT NULL,
  `total_count` bigint DEFAULT '0',
  `failed_count` bigint DEFAULT '0',
  `passed_count` bigint DEFAULT '0',
  `aborted_count` bigint DEFAULT '0',
  `stopped_count` bigint DEFAULT '0',
  `not_executed_count` bigint DEFAULT '0',
  `queued_count` bigint DEFAULT '0',
  `is_visually_passed` bit(1) DEFAULT NULL,
  `session_id` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `re_run_parent_id` bigint DEFAULT NULL,
  `platform_assets_endpoint_url` text COLLATE utf8mb3_unicode_ci,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_case_results_on_test_device_result_id` (`test_device_result_id`),
  KEY `index_test_case_results_on_env_run_id_and_suite_result_id` (`test_device_result_id`,`suite_result_id`),
  KEY `index_test_case_results_on_test_plan_result_id` (`test_plan_result_id`),
  KEY `index_test_case_results_on_parent_id` (`parent_id`),
  KEY `index_test_case_results_on_suite_result_id` (`suite_result_id`),
  KEY `index_test_case_results_on_result` (`result`),
  KEY `index_test_case_results_on_iteration` (`iteration`),
  KEY `index_test_case_results_on_test_case_id` (`test_case_id`),
  KEY `index_test_case_results_on_re_run_parent_id` (`re_run_parent_id`),
  KEY `fk_test_data_id_in_test_case_results_to_test_data` (`test_data_id`),
  CONSTRAINT `fk_env_run_id_in_test_case_results_to_test_device_results` FOREIGN KEY (`test_device_result_id`) REFERENCES `test_device_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_suite_result_id_in_test_case_results_to_test_suite_results` FOREIGN KEY (`suite_result_id`) REFERENCES `test_suite_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_data_id_in_test_case_results_to_test_data` FOREIGN KEY (`test_data_id`) REFERENCES `test_data` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_test_plan_result_id_in_test_case_results_to_test_plan_results` FOREIGN KEY (`test_plan_result_id`) REFERENCES `test_plan_results` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3369 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_case_types`
--

DROP TABLE IF EXISTS `test_case_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_case_types` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `display_name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `workspace_id` bigint NOT NULL,
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_test_case_types_on_name_and_workspace_id` (`name`,`workspace_id`),
  KEY `index_test_case_types_on_workspace_id` (`workspace_id`),
  CONSTRAINT `fk_workspace_id_in_test_case_types_to_workspaces` FOREIGN KEY (`workspace_id`) REFERENCES `workspaces` (`id`) ON DELETE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_cases`
--

DROP TABLE IF EXISTS `test_cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_cases` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `is_data_driven` bit(1) NOT NULL DEFAULT b'0',
  `is_step_group` bit(1) NOT NULL DEFAULT b'0',
  `is_active` tinyint(1) DEFAULT '1',
  `priority_id` bigint DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `type` bigint DEFAULT NULL,
  `test_data_id` bigint DEFAULT NULL,
  `workspace_version_id` bigint DEFAULT NULL,
  `pre_requisite` bigint DEFAULT NULL,
  `copied_from` bigint DEFAULT NULL,
  `deleted` bit(1) DEFAULT b'0',
  `test_data_start_index` int DEFAULT '0',
  `test_data_end_index` int DEFAULT NULL,
  `last_run_id` bigint DEFAULT NULL,
  `draft_at` datetime DEFAULT NULL,
  `obsolete_at` datetime DEFAULT NULL,
  `ready_at` datetime DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `test_cases_unique_name` (`workspace_version_id`,`name`,`is_active`),
  KEY `index_on_test_cases_priority_id` (`priority_id`),
  KEY `index_on_test_cases_type` (`type`),
  KEY `index_on_test_cases_workspace_version_id` (`workspace_version_id`),
  KEY `index_on_test_cases_status` (`status`),
  KEY `index_on_test_cases_is_step_group` (`is_step_group`),
  KEY `fk_test_data_id_in_test_cases_to_test_data` (`test_data_id`),
  KEY `last_run_id_on_test_case` (`last_run_id`),
  CONSTRAINT `fk_priority_id_in_test_cases_to_test_case_priorities` FOREIGN KEY (`priority_id`) REFERENCES `test_case_priorities` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_test_data_id_in_test_cases_to_test_data` FOREIGN KEY (`test_data_id`) REFERENCES `test_data` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_type_in_test_cases_to_test_case_types` FOREIGN KEY (`type`) REFERENCES `test_case_types` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `test_cases_ibfk_1` FOREIGN KEY (`last_run_id`) REFERENCES `test_case_results` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=222 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_data`
--

DROP TABLE IF EXISTS `test_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_data` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `version_id` bigint DEFAULT NULL,
  `test_data` mediumtext COLLATE utf8mb3_unicode_ci,
  `test_data_name` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `copied_from` bigint DEFAULT NULL,
  `passwords` json DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `is_migrated` tinyint(1) DEFAULT '0',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_test_data_on_version_id_and_test_data_name` (`version_id`,`test_data_name`),
  KEY `index_test_data_on_version_id` (`version_id`),
  CONSTRAINT `fk_version_id_in_test_data_to_workspace_versions` FOREIGN KEY (`version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_data_sets`
--

DROP TABLE IF EXISTS `test_data_sets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_data_sets` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_data_id` bigint NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `description` mediumtext COLLATE utf8mb3_unicode_ci,
  `expected_to_fail` tinyint(1) DEFAULT '0',
  `data` mediumtext COLLATE utf8mb3_unicode_ci NOT NULL,
  `position` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_test_data_profile_id_td_sets` (`test_data_id`),
  CONSTRAINT `test_data_sets_ibfk_1` FOREIGN KEY (`test_data_id`) REFERENCES `test_data` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_device_results`
--

DROP TABLE IF EXISTS `test_device_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_device_results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_device_id` bigint DEFAULT NULL,
  `duration` bigint DEFAULT NULL,
  `test_plan_result_id` bigint NOT NULL,
  `start_time` timestamp NULL DEFAULT NULL,
  `end_time` timestamp NULL DEFAULT NULL,
  `result` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `browser_version` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `message` text COLLATE utf8mb3_unicode_ci,
  `agent_start_time` timestamp NULL DEFAULT NULL,
  `agent_end_time` timestamp NULL DEFAULT NULL,
  `app_upload_version_id` bigint DEFAULT NULL,
  `environment_settings` json DEFAULT NULL,
  `execution_initiated_on` timestamp NULL DEFAULT NULL,
  `agent_picked_on` timestamp NULL DEFAULT NULL,
  `device_allocated_on` timestamp NULL DEFAULT NULL,
  `session_created_on` timestamp NULL DEFAULT NULL,
  `session_completed_on` timestamp NULL DEFAULT NULL,
  `total_count` bigint DEFAULT '0',
  `failed_count` bigint DEFAULT '0',
  `passed_count` bigint DEFAULT '0',
  `aborted_count` bigint DEFAULT '0',
  `stopped_count` bigint DEFAULT '0',
  `not_executed_count` bigint DEFAULT '0',
  `queued_count` bigint DEFAULT '0',
  `is_visually_passed` bit(1) DEFAULT NULL,
  `session_id` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `re_run_parent_id` bigint DEFAULT NULL,
  `prerequisite_test_device_result_id` bigint DEFAULT NULL,
  `test_lab_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `workspace_version_id` bigint DEFAULT NULL,
  `platform_assets_endpoint_url` text COLLATE utf8mb3_unicode_ci,
  `queued` tinyint(1) DEFAULT '0',
  `initiated` tinyint(1) DEFAULT '0',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_device_results_on_test_plan_result_id` (`test_plan_result_id`),
  KEY `index_test_device_results_on_status_index` (`status`),
  KEY `index_test_device_results_on_result_index` (`result`),
  KEY `index_test_device_results_on_re_run_parent_id_index` (`re_run_parent_id`),
  KEY `fk_workspace_version_id_in_device_results_to_workspace_versions` (`workspace_version_id`),
  CONSTRAINT `fk_test_plan_run_id_in_test_device_results_to_test_plan_results` FOREIGN KEY (`test_plan_result_id`) REFERENCES `test_plan_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_workspace_version_id_in_device_results_to_workspace_versions` FOREIGN KEY (`workspace_version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=262 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_device_suites`
--

DROP TABLE IF EXISTS `test_device_suites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_device_suites` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_device_id` bigint DEFAULT NULL,
  `suite_id` bigint DEFAULT NULL,
  `order_id` int DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_test_device_suites_on_test_device_id_and_suite_id` (`test_device_id`,`suite_id`),
  KEY `index_test_device_suites_on_test_device_id` (`test_device_id`),
  KEY `index_test_device_suites_on_suite_id` (`suite_id`),
  CONSTRAINT `fk_suite_id_in_test_device_suites_to_test_suites` FOREIGN KEY (`suite_id`) REFERENCES `test_suites` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_device_id_in_test_device_suites_to_test_devices` FOREIGN KEY (`test_device_id`) REFERENCES `test_devices` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=174 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_devices`
--

DROP TABLE IF EXISTS `test_devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_devices` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(250) COLLATE utf8mb3_unicode_ci NOT NULL,
  `test_plan_id` bigint DEFAULT NULL,
  `agent_id` bigint DEFAULT NULL,
  `device_id` bigint DEFAULT NULL,
  `browser` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `platform` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `browser_version` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `platform_device_id` bigint DEFAULT NULL,
  `udid` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_upload_id` bigint DEFAULT NULL,
  `app_upload_version_id` bigint DEFAULT NULL,
  `app_package` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_activity` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_url` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_bundle_id` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `app_path_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `capabilities` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `platform_screen_resolution_id` bigint DEFAULT NULL,
  `platform_browser_version_id` bigint DEFAULT NULL,
  `platform_os_version_id` bigint DEFAULT NULL,
  `prerequisite_test_devices_id` bigint DEFAULT NULL,
  `workspace_version_id` bigint DEFAULT NULL,
  `test_lab_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `disabled` bit(1) NOT NULL DEFAULT b'0',
  `match_browser_version` tinyint(1) DEFAULT '0',
  `copied_from` bigint DEFAULT NULL,
  `create_session_at_case_level` tinyint(1) NOT NULL DEFAULT '0',
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_devices_on_test_plan_id` (`test_plan_id`),
  KEY `index_test_devices_on_agent_id` (`agent_id`),
  KEY `fk_workspace_version_id_in_test_devices_to_workspace_versions` (`workspace_version_id`),
  CONSTRAINT `fk_agent_id_in_test_devices_to_uploads` FOREIGN KEY (`agent_id`) REFERENCES `agents` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_test_plan_id_in_test_devices_to_test_plans` FOREIGN KEY (`test_plan_id`) REFERENCES `test_plans` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_workspace_version_id_in_test_devices_to_workspace_versions` FOREIGN KEY (`workspace_version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=384 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_plan_results`
--

DROP TABLE IF EXISTS `test_plan_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_plan_results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_plan_id` bigint NOT NULL,
  `start_time` timestamp NULL DEFAULT NULL,
  `end_time` timestamp NULL DEFAULT NULL,
  `duration` bigint DEFAULT NULL,
  `result` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `message` text COLLATE utf8mb3_unicode_ci,
  `build_no` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `environment_id` bigint DEFAULT NULL,
  `test_plan_details` json DEFAULT NULL,
  `is_in_progress` bit(1) DEFAULT b'0',
  `total_count` bigint DEFAULT '0',
  `failed_count` bigint DEFAULT '0',
  `passed_count` bigint DEFAULT '0',
  `aborted_count` bigint DEFAULT '0',
  `stopped_count` bigint DEFAULT '0',
  `not_executed_count` bigint DEFAULT '0',
  `queued_count` bigint DEFAULT '0',
  `is_visually_passed` bit(1) DEFAULT NULL,
  `re_run_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `re_run_parent_id` bigint DEFAULT NULL,
  `triggered_type` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `scheduled_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_plan_results_on_test_plan_id` (`test_plan_id`),
  KEY `index_test_plan_results_on_environment_id` (`environment_id`),
  KEY `index_test_plan_results_on_status_index` (`status`),
  KEY `index_test_plan_results_on_result_index` (`result`),
  KEY `index_test_plan_results_on_start_time_index` (`start_time`),
  KEY `index_test_plan_results_on_re_run_parent_id_index` (`re_run_parent_id`),
  KEY `index_test_plan_results_on_scheduled_id` (`scheduled_id`),
  CONSTRAINT `fk_environment_id_in_test_plan_results_to_environments` FOREIGN KEY (`environment_id`) REFERENCES `environments` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_scheduled_id_in_test_plan_results_to_schedule_test_plans` FOREIGN KEY (`scheduled_id`) REFERENCES `schedule_test_plans` (`id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_test_plan_id_in_test_plan_results_to_test_plans` FOREIGN KEY (`test_plan_id`) REFERENCES `test_plans` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=242 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_plans`
--

DROP TABLE IF EXISTS `test_plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_plans` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `workspace_version_id` bigint DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `element_time_out` int unsigned DEFAULT '0',
  `environment_id` bigint DEFAULT NULL,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `page_time_out` int unsigned DEFAULT '0',
  `screenshot` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `recovery_action` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `on_aborted_action` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `re_run_on_failure` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `on_suite_pre_requisite_failed` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `on_testcase_pre_requisite_failed` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `on_step_pre_requisite_failed` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  `retry_session_timeout` int DEFAULT '0',
  `retry_session_creation` bit(1) DEFAULT b'0',
  `test_lab_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `test_plan_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT 'DISTRIBUTED',
  `last_run_id` bigint DEFAULT NULL,
  `match_browser_version` tinyint(1) DEFAULT '0',
  `copied_from` bigint DEFAULT NULL,
  `entity_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT 'TEST_PLAN',
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_test_plans_on_workspace_version_id_and_name` (`workspace_version_id`,`name`),
  KEY `index_test_plans_on_workspace_version_id` (`workspace_version_id`),
  KEY `index_test_plans_on_environment_id` (`environment_id`),
  KEY `last_run_id_on_test_plan` (`last_run_id`),
  CONSTRAINT `fk_environment_id_in_test_plans_to_environments` FOREIGN KEY (`environment_id`) REFERENCES `environments` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `fk_workspace_version_id_in_test_plans_to_workspace_versions` FOREIGN KEY (`workspace_version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE,
  CONSTRAINT `test_plans_ibfk_1` FOREIGN KEY (`last_run_id`) REFERENCES `test_plan_results` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=324 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_step_result_screenshot_comparisons`
--

DROP TABLE IF EXISTS `test_step_result_screenshot_comparisons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_step_result_screenshot_comparisons` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_step_id` bigint NOT NULL,
  `test_case_result_id` bigint DEFAULT NULL,
  `test_step_result_id` bigint DEFAULT NULL,
  `test_step_screenshot_id` bigint DEFAULT NULL,
  `similarity_score` decimal(6,3) DEFAULT NULL,
  `diff_coordinates` longtext COLLATE utf8mb3_unicode_ci,
  `image_shape` varchar(32) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `error_message` longtext COLLATE utf8mb3_unicode_ci,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_test_step_id_and_test_step_result_id` (`test_step_id`,`test_step_result_id`),
  KEY `index_test_step_id` (`test_step_id`),
  KEY `index_test_step_result_id` (`test_step_result_id`),
  KEY `index_test_step_screenshot_id` (`test_step_screenshot_id`),
  KEY `index_test_case_result_id` (`test_case_result_id`),
  CONSTRAINT `fk_test_step_id_to_test_steps` FOREIGN KEY (`test_step_id`) REFERENCES `test_steps` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_step_result_id_to_test_step_results` FOREIGN KEY (`test_step_result_id`) REFERENCES `test_step_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_step_screenshot_id_to_test_step_screenshots` FOREIGN KEY (`test_step_screenshot_id`) REFERENCES `test_step_screenshots` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_step_results`
--

DROP TABLE IF EXISTS `test_step_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_step_results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_device_result_id` bigint NOT NULL,
  `test_case_id` bigint NOT NULL,
  `step_id` bigint NOT NULL,
  `step_group_id` bigint DEFAULT NULL,
  `result` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `error_code` int DEFAULT NULL,
  `message` text COLLATE utf8mb3_unicode_ci,
  `metadata` longtext COLLATE utf8mb3_unicode_ci,
  `start_time` timestamp NULL DEFAULT NULL,
  `end_time` timestamp NULL DEFAULT NULL,
  `duration` bigint DEFAULT NULL,
  `test_case_result_id` bigint DEFAULT NULL,
  `step_group_result_id` bigint DEFAULT NULL,
  `screenshot_name` text COLLATE utf8mb3_unicode_ci,
  `parent_result_id` bigint DEFAULT NULL,
  `web_driver_exception` text COLLATE utf8mb3_unicode_ci,
  `priority` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `test_step_details` json DEFAULT NULL,
  `element_details` json DEFAULT NULL,
  `test_data_details` json DEFAULT NULL,
  `visual_enabled` tinyint(1) DEFAULT '0',
  `wait_time` bigint DEFAULT NULL,
  `addon_test_data` json DEFAULT NULL,
  `addon_elements` json DEFAULT NULL,
  `addon_action_logs` longtext COLLATE utf8mb3_unicode_ci,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_step_results_on_step_id` (`step_id`),
  KEY `index_test_step_results_on_test_device_result_id` (`test_device_result_id`),
  KEY `index_test_step_results_on_test_case_result_id` (`test_case_result_id`),
  KEY `index_test_step_results_on_step_group_result_id` (`step_group_result_id`),
  CONSTRAINT `fk_env_run_id_in_test_step_results_to_test_device_results` FOREIGN KEY (`test_device_result_id`) REFERENCES `test_device_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_case_result_id_in_test_step_results_to_test_case_results` FOREIGN KEY (`test_case_result_id`) REFERENCES `test_case_results` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=30098 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_step_screenshots`
--

DROP TABLE IF EXISTS `test_step_screenshots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_step_screenshots` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_step_id` bigint NOT NULL,
  `test_step_result_id` bigint DEFAULT NULL,
  `test_device_result_id` bigint NOT NULL,
  `testcase_result_id` bigint NOT NULL,
  `base_image_size` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `entity_type` varchar(30) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `test_data_set_name` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `test_data_id` bigint DEFAULT NULL,
  `base_image_name` text COLLATE utf8mb3_unicode_ci,
  `screen_resolution` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `browser` varchar(50) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `browser_version` double(20,2) DEFAULT NULL,
  `ignored_coordinates` longtext COLLATE utf8mb3_unicode_ci,
  `device_os_version` varchar(16) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `device_name` varchar(128) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_step_screenshots_on_test_step_id` (`test_step_id`),
  KEY `index_test_step_screenshots_on_test_device_result_id` (`test_device_result_id`),
  KEY `index_test_step_screenshots_on_testcase_result_id` (`testcase_result_id`),
  KEY `index_test_step_screenshots_on_test_step_result_id` (`test_step_result_id`),
  CONSTRAINT `fk_test_case_result_id_in_screenshots_to_test_case_results` FOREIGN KEY (`testcase_result_id`) REFERENCES `test_case_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_device_result_id_in_screenshots_to_test_device_results` FOREIGN KEY (`test_device_result_id`) REFERENCES `test_device_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_step_id_in_test_step_screenshots_to_test_steps` FOREIGN KEY (`test_step_id`) REFERENCES `test_steps` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_step_result_id_in_screenshots_to_test_step_results` FOREIGN KEY (`test_step_result_id`) REFERENCES `test_step_results` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_steps`
--

DROP TABLE IF EXISTS `test_steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_steps` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `action` text COLLATE utf8mb3_unicode_ci,
  `pre_requisite` bigint DEFAULT NULL,
  `priority` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT 'NOT_USED',
  `step_id` bigint DEFAULT NULL,
  `test_case_id` bigint DEFAULT NULL,
  `step_group_id` bigint DEFAULT NULL,
  `natural_text_action_id` int unsigned DEFAULT '0',
  `type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT 'ACTION_TEXT',
  `addon_test_data` json DEFAULT NULL,
  `addon_elements` json DEFAULT NULL,
  `condition_if` json DEFAULT NULL,
  `test_data` json DEFAULT NULL,
  `element` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `attribute` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `for_loop_start_index` int DEFAULT NULL,
  `for_loop_end_index` int DEFAULT NULL,
  `for_loop_test_data_id` bigint DEFAULT NULL,
  `addon_test_data_function` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `test_data_function_id` bigint DEFAULT NULL,
  `test_data_function_args` json DEFAULT NULL,
  `max_iterations` bigint DEFAULT NULL,
  `wait_time` int DEFAULT NULL,
  `condition_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `parent_id` bigint DEFAULT NULL,
  `copied_from` bigint DEFAULT NULL,
  `disabled` tinyint(1) DEFAULT '0',
  `visual_enabled` tinyint(1) DEFAULT '0',
  `ignore_step_result` tinyint(1) DEFAULT '0',
  `addon_plugin_tdf_data` longtext COLLATE utf8mb3_unicode_ci,
  `addon_natural_text_action_data` json DEFAULT NULL,
  `addon_action_id` bigint DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `test_data_profile_step_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_steps_on_test_case_id` (`test_case_id`),
  KEY `step_group_id` (`step_group_id`),
  CONSTRAINT `fk_step_group_id_in_test_steps_to_test_cases` FOREIGN KEY (`test_case_id`) REFERENCES `test_cases` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_case_id_in_test_steps_to_test_cases` FOREIGN KEY (`step_group_id`) REFERENCES `test_cases` (`id`) ON DELETE CASCADE,
  CONSTRAINT `test_steps_ibfk_1` FOREIGN KEY (`step_group_id`) REFERENCES `test_cases` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1463 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_suite_cases`
--

DROP TABLE IF EXISTS `test_suite_cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_suite_cases` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `suite_id` bigint NOT NULL,
  `test_case_id` bigint NOT NULL,
  `position` bigint DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_suite_cases_on_suite_id` (`suite_id`),
  KEY `index_test_suite_cases_on_test_case_id` (`test_case_id`),
  CONSTRAINT `fk_suite_id_in_test_suite_cases_to_test_suites` FOREIGN KEY (`suite_id`) REFERENCES `test_suites` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_case_id_in_test_suite_cases_to_test_cases` FOREIGN KEY (`test_case_id`) REFERENCES `test_cases` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=189 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_suite_results`
--

DROP TABLE IF EXISTS `test_suite_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_suite_results` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_plan_result_id` bigint DEFAULT NULL,
  `test_device_result_id` bigint NOT NULL,
  `suite_id` bigint NOT NULL,
  `result` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `message` text COLLATE utf8mb3_unicode_ci,
  `start_time` timestamp NULL DEFAULT NULL,
  `end_time` timestamp NULL DEFAULT NULL,
  `duration` bigint DEFAULT NULL,
  `order_id` int DEFAULT NULL,
  `suite_details` json DEFAULT NULL,
  `started` bit(1) DEFAULT NULL,
  `execution_initiated_on` timestamp NULL DEFAULT NULL,
  `agent_picked_on` timestamp NULL DEFAULT NULL,
  `device_allocated_on` timestamp NULL DEFAULT NULL,
  `session_created_on` timestamp NULL DEFAULT NULL,
  `session_completed_on` timestamp NULL DEFAULT NULL,
  `total_count` bigint DEFAULT '0',
  `failed_count` bigint DEFAULT '0',
  `passed_count` bigint DEFAULT '0',
  `aborted_count` bigint DEFAULT '0',
  `stopped_count` bigint DEFAULT '0',
  `not_executed_count` bigint DEFAULT '0',
  `queued_count` bigint DEFAULT '0',
  `is_visually_passed` bit(1) DEFAULT NULL,
  `session_id` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `re_run_parent_id` bigint DEFAULT NULL,
  `platform_assets_endpoint_url` text COLLATE utf8mb3_unicode_ci,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `index_test_suite_results_on_test_device_result_id` (`test_device_result_id`),
  KEY `index_test_suite_results_on_test_plan_result_id` (`test_plan_result_id`),
  KEY `index_test_suite_results_on_re_run_parent_id` (`re_run_parent_id`),
  CONSTRAINT `fk_test_device_result_id_to_test_device_results` FOREIGN KEY (`test_device_result_id`) REFERENCES `test_device_results` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_test_plan_result_id_to_test_plan_results` FOREIGN KEY (`test_plan_result_id`) REFERENCES `test_plan_results` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `test_suites`
--

DROP TABLE IF EXISTS `test_suites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_suites` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `action_id` bigint DEFAULT NULL,
  `workspace_version_id` bigint DEFAULT NULL,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `pre_requisite` bigint DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `copied_from` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `entity_type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `last_run_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_test_suites_on_workspace_version_id_and_name` (`workspace_version_id`,`name`),
  KEY `index_test_suites_on_workspace_version_id` (`workspace_version_id`),
  KEY `last_run_id_on_test_case_group` (`last_run_id`),
  CONSTRAINT `fk_workspace_version_id_in_test_suites_to_workspace_versions` FOREIGN KEY (`workspace_version_id`) REFERENCES `workspace_versions` (`id`) ON DELETE CASCADE,
  CONSTRAINT `test_suites_ibfk_1` FOREIGN KEY (`last_run_id`) REFERENCES `test_suite_results` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `testsigma_os_config`
--

DROP TABLE IF EXISTS `testsigma_os_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testsigma_os_config` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_name` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `access_key` varchar(1000) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `upload_versions`
--

DROP TABLE IF EXISTS `upload_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `upload_versions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `path` text COLLATE utf8mb3_unicode_ci,
  `file_name` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `type` varchar(100) COLLATE utf8mb3_unicode_ci NOT NULL,
  `version` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `file_size` int DEFAULT NULL,
  `upload_id` bigint DEFAULT NULL,
  `workspace_id` bigint DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `version_name` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `bundle_id` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `activity` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `package_name` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `upload_status` varchar(100) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `last_uploaded_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uploads_upload_id_name` (`upload_id`,`name`),
  CONSTRAINT `fk_upload_versions_upload_id` FOREIGN KEY (`upload_id`) REFERENCES `uploads` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `uploads`
--

DROP TABLE IF EXISTS `uploads`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uploads` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(256) DEFAULT NULL,
  `workspace_id` bigint DEFAULT NULL,
  `latest_version_id` bigint DEFAULT NULL,
  `imported_id` bigint DEFAULT NULL,
  `supported_device` varchar(256) DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_uploads_on_workspace_id_and_name` (`workspace_id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user_preferences`
--

DROP TABLE IF EXISTS `user_preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_preferences` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(256) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `version_id` bigint DEFAULT NULL,
  `test_case_filter_id` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `showed_github_star` bit(1) DEFAULT b'0',
  `clicked_skip_for_now` smallint DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_user_preferences_on_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `workspace_versions`
--

DROP TABLE IF EXISTS `workspace_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workspace_versions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `workspace_id` bigint DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `version_name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `copied_from` bigint DEFAULT NULL,
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_workspace_versions_on_workspace_id_and_version_name` (`workspace_id`,`version_name`),
  KEY `index_workspace_versions_on_workspace_id` (`workspace_id`),
  CONSTRAINT `fk_workspace_id_in_workspace_versions_to_workspaces` FOREIGN KEY (`workspace_id`) REFERENCES `workspaces` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `workspaces`
--

DROP TABLE IF EXISTS `workspaces`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workspaces` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `type` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `description` text COLLATE utf8mb3_unicode_ci,
  `name` varchar(250) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `is_demo` tinyint(1) DEFAULT '0',
  `created_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_workspaces_on_name` (`name`),
  UNIQUE KEY `index_workspace_on_type_and_is_demo` (`type`,`is_demo`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-09 16:49:48

---
title: sql
hide_title: false
hide_table_of_contents: false
keywords:
  - sql
  - azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
SQL  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure.sql</code></td></tr>
<tr><td><b>Type</b></td><td>Service</td></tr>
<tr><td><b>Title</b></td><td>SQL (Microsoft.Sql)</td></tr>
<tr><td><b>Description</b></td><td>SQL</td></tr>
<tr><td><b>Id</b></td><td><code>sql:v0.3.0</code></td></tr>
</tbody></table>

## Resources
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure/sql/agent/">agent</a><br />
<a href="/providers/azure/sql/backup_short_term_retention_policies/">backup_short_term_retention_policies</a><br />
<a href="/providers/azure/sql/capabilities/">capabilities</a><br />
<a href="/providers/azure/sql/data_masking_policies/">data_masking_policies</a><br />
<a href="/providers/azure/sql/data_masking_rules/">data_masking_rules</a><br />
<a href="/providers/azure/sql/data_warehouse_user_activities/">data_warehouse_user_activities</a><br />
<a href="/providers/azure/sql/database_advanced_threat_protection_settings/">database_advanced_threat_protection_settings</a><br />
<a href="/providers/azure/sql/database_advisors/">database_advisors</a><br />
<a href="/providers/azure/sql/database_automatic_tuning/">database_automatic_tuning</a><br />
<a href="/providers/azure/sql/database_blob_auditing_policies/">database_blob_auditing_policies</a><br />
<a href="/providers/azure/sql/database_columns/">database_columns</a><br />
<a href="/providers/azure/sql/database_extensions/">database_extensions</a><br />
<a href="/providers/azure/sql/database_operations/">database_operations</a><br />
<a href="/providers/azure/sql/database_recommended_actions/">database_recommended_actions</a><br />
<a href="/providers/azure/sql/database_schemas/">database_schemas</a><br />
<a href="/providers/azure/sql/database_security_alert_policies/">database_security_alert_policies</a><br />
<a href="/providers/azure/sql/database_sql_vulnerability_assessment_baselines/">database_sql_vulnerability_assessment_baselines</a><br />
<a href="/providers/azure/sql/database_sql_vulnerability_assessment_execute_scan/">database_sql_vulnerability_assessment_execute_scan</a><br />
<a href="/providers/azure/sql/database_sql_vulnerability_assessment_rule_baselines/">database_sql_vulnerability_assessment_rule_baselines</a><br />
<a href="/providers/azure/sql/database_sql_vulnerability_assessment_scan_result/">database_sql_vulnerability_assessment_scan_result</a><br />
<a href="/providers/azure/sql/database_sql_vulnerability_assessment_scans/">database_sql_vulnerability_assessment_scans</a><br />
<a href="/providers/azure/sql/database_sql_vulnerability_assessments_settings/">database_sql_vulnerability_assessments_settings</a><br />
<a href="/providers/azure/sql/database_tables/">database_tables</a><br />
<a href="/providers/azure/sql/database_usages/">database_usages</a><br />
<a href="/providers/azure/sql/database_vulnerability_assessment_rule_baselines/">database_vulnerability_assessment_rule_baselines</a><br />
<a href="/providers/azure/sql/database_vulnerability_assessment_scans/">database_vulnerability_assessment_scans</a><br />
<a href="/providers/azure/sql/database_vulnerability_assessments/">database_vulnerability_assessments</a><br />
<a href="/providers/azure/sql/databases/">databases</a><br />
<a href="/providers/azure/sql/deleted_servers/">deleted_servers</a><br />
<a href="/providers/azure/sql/distributed_availability_groups/">distributed_availability_groups</a><br />
<a href="/providers/azure/sql/elastic_pool_activities/">elastic_pool_activities</a><br />
<a href="/providers/azure/sql/elastic_pool_database_activities/">elastic_pool_database_activities</a><br />
<a href="/providers/azure/sql/elastic_pool_operations/">elastic_pool_operations</a><br />
<a href="/providers/azure/sql/elastic_pools/">elastic_pools</a><br />
<a href="/providers/azure/sql/encryption_protectors/">encryption_protectors</a><br />
<a href="/providers/azure/sql/endpoint_certificates/">endpoint_certificates</a><br />
<a href="/providers/azure/sql/extended_database_blob_auditing_policies/">extended_database_blob_auditing_policies</a><br />
<a href="/providers/azure/sql/extended_server_blob_auditing_policies/">extended_server_blob_auditing_policies</a><br />
<a href="/providers/azure/sql/failover_groups/">failover_groups</a><br />
<a href="/providers/azure/sql/firewall_rules/">firewall_rules</a><br />
<a href="/providers/azure/sql/geo_backup_policies/">geo_backup_policies</a><br />
<a href="/providers/azure/sql/i_pv6_firewall_rules/">i_pv6_firewall_rules</a><br />
<a href="/providers/azure/sql/instance_failover_groups/">instance_failover_groups</a><br />
<a href="/providers/azure/sql/instance_pools/">instance_pools</a><br />
<a href="/providers/azure/sql/job_agents/">job_agents</a><br />
<a href="/providers/azure/sql/job_credentials/">job_credentials</a><br />
<a href="/providers/azure/sql/job_executions/">job_executions</a><br />
<a href="/providers/azure/sql/job_step_executions/">job_step_executions</a><br />
<a href="/providers/azure/sql/job_steps/">job_steps</a><br />
<a href="/providers/azure/sql/job_target_executions/">job_target_executions</a><br />
<a href="/providers/azure/sql/job_target_groups/">job_target_groups</a><br />
<a href="/providers/azure/sql/job_versions/">job_versions</a><br />
<a href="/providers/azure/sql/jobs/">jobs</a><br />
<a href="/providers/azure/sql/ledger_digest_uploads/">ledger_digest_uploads</a><br />
<a href="/providers/azure/sql/long_term_retention_backups/">long_term_retention_backups</a><br />
<a href="/providers/azure/sql/long_term_retention_managed_instance_backups/">long_term_retention_managed_instance_backups</a><br />
<a href="/providers/azure/sql/long_term_retention_policies/">long_term_retention_policies</a><br />
<a href="/providers/azure/sql/maintenance_window_options/">maintenance_window_options</a><br />
<a href="/providers/azure/sql/maintenance_windows/">maintenance_windows</a><br />
<a href="/providers/azure/sql/managed_backup_short_term_retention_policies/">managed_backup_short_term_retention_policies</a><br />
<a href="/providers/azure/sql/managed_database_advanced_threat_protection_settings/">managed_database_advanced_threat_protection_settings</a><br />
<a href="/providers/azure/sql/managed_database_columns/">managed_database_columns</a><br />
<a href="/providers/azure/sql/managed_database_move_operations/">managed_database_move_operations</a><br />
<a href="/providers/azure/sql/managed_database_queries/">managed_database_queries</a><br />
<a href="/providers/azure/sql/managed_database_recommended_sensitivity_labels/">managed_database_recommended_sensitivity_labels</a><br />
<a href="/providers/azure/sql/managed_database_restore_details/">managed_database_restore_details</a><br />
<a href="/providers/azure/sql/managed_database_schemas/">managed_database_schemas</a><br />
<a href="/providers/azure/sql/managed_database_security_alert_policies/">managed_database_security_alert_policies</a><br />
<a href="/providers/azure/sql/managed_database_security_events/">managed_database_security_events</a><br />
<a href="/providers/azure/sql/managed_database_sensitivity_labels/">managed_database_sensitivity_labels</a><br />
<a href="/providers/azure/sql/managed_database_tables/">managed_database_tables</a><br />
<a href="/providers/azure/sql/managed_database_transparent_data_encryption/">managed_database_transparent_data_encryption</a><br />
<a href="/providers/azure/sql/managed_database_vulnerability_assessment_rule_baselines/">managed_database_vulnerability_assessment_rule_baselines</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure/sql/managed_database_vulnerability_assessment_scans/">managed_database_vulnerability_assessment_scans</a><br />
<a href="/providers/azure/sql/managed_database_vulnerability_assessments/">managed_database_vulnerability_assessments</a><br />
<a href="/providers/azure/sql/managed_databases/">managed_databases</a><br />
<a href="/providers/azure/sql/managed_instance_administrators/">managed_instance_administrators</a><br />
<a href="/providers/azure/sql/managed_instance_advanced_threat_protection_settings/">managed_instance_advanced_threat_protection_settings</a><br />
<a href="/providers/azure/sql/managed_instance_azure_ad_only_authentications/">managed_instance_azure_ad_only_authentications</a><br />
<a href="/providers/azure/sql/managed_instance_dtcs/">managed_instance_dtcs</a><br />
<a href="/providers/azure/sql/managed_instance_encryption_protectors/">managed_instance_encryption_protectors</a><br />
<a href="/providers/azure/sql/managed_instance_keys/">managed_instance_keys</a><br />
<a href="/providers/azure/sql/managed_instance_long_term_retention_policies/">managed_instance_long_term_retention_policies</a><br />
<a href="/providers/azure/sql/managed_instance_operations/">managed_instance_operations</a><br />
<a href="/providers/azure/sql/managed_instance_private_endpoint_connections/">managed_instance_private_endpoint_connections</a><br />
<a href="/providers/azure/sql/managed_instance_private_link_resources/">managed_instance_private_link_resources</a><br />
<a href="/providers/azure/sql/managed_instance_tde_certificates/">managed_instance_tde_certificates</a><br />
<a href="/providers/azure/sql/managed_instance_vulnerability_assessments/">managed_instance_vulnerability_assessments</a><br />
<a href="/providers/azure/sql/managed_instances/">managed_instances</a><br />
<a href="/providers/azure/sql/managed_restorable_dropped_database_backup_short_term_retention_policies/">managed_restorable_dropped_database_backup_short_term_retention_policies</a><br />
<a href="/providers/azure/sql/managed_server_dns_aliases/">managed_server_dns_aliases</a><br />
<a href="/providers/azure/sql/managed_server_security_alert_policies/">managed_server_security_alert_policies</a><br />
<a href="/providers/azure/sql/operations/">operations</a><br />
<a href="/providers/azure/sql/outbound_firewall_rules/">outbound_firewall_rules</a><br />
<a href="/providers/azure/sql/private_endpoint_connections/">private_endpoint_connections</a><br />
<a href="/providers/azure/sql/private_link_resources/">private_link_resources</a><br />
<a href="/providers/azure/sql/recommended_sensitivity_labels/">recommended_sensitivity_labels</a><br />
<a href="/providers/azure/sql/recoverable_databases/">recoverable_databases</a><br />
<a href="/providers/azure/sql/recoverable_managed_databases/">recoverable_managed_databases</a><br />
<a href="/providers/azure/sql/replication_links/">replication_links</a><br />
<a href="/providers/azure/sql/restorable_dropped_databases/">restorable_dropped_databases</a><br />
<a href="/providers/azure/sql/restorable_dropped_managed_databases/">restorable_dropped_managed_databases</a><br />
<a href="/providers/azure/sql/restore_points/">restore_points</a><br />
<a href="/providers/azure/sql/sensitivity_labels/">sensitivity_labels</a><br />
<a href="/providers/azure/sql/server_advanced_threat_protection_settings/">server_advanced_threat_protection_settings</a><br />
<a href="/providers/azure/sql/server_advisors/">server_advisors</a><br />
<a href="/providers/azure/sql/server_automatic_tuning/">server_automatic_tuning</a><br />
<a href="/providers/azure/sql/server_azure_ad_administrators/">server_azure_ad_administrators</a><br />
<a href="/providers/azure/sql/server_azure_ad_only_authentications/">server_azure_ad_only_authentications</a><br />
<a href="/providers/azure/sql/server_blob_auditing_policies/">server_blob_auditing_policies</a><br />
<a href="/providers/azure/sql/server_communication_links/">server_communication_links</a><br />
<a href="/providers/azure/sql/server_connection_policies/">server_connection_policies</a><br />
<a href="/providers/azure/sql/server_dev_ops_audit_settings/">server_dev_ops_audit_settings</a><br />
<a href="/providers/azure/sql/server_dns_aliases/">server_dns_aliases</a><br />
<a href="/providers/azure/sql/server_keys/">server_keys</a><br />
<a href="/providers/azure/sql/server_operations/">server_operations</a><br />
<a href="/providers/azure/sql/server_security_alert_policies/">server_security_alert_policies</a><br />
<a href="/providers/azure/sql/server_trust_certificates/">server_trust_certificates</a><br />
<a href="/providers/azure/sql/server_trust_groups/">server_trust_groups</a><br />
<a href="/providers/azure/sql/server_usages/">server_usages</a><br />
<a href="/providers/azure/sql/server_vulnerability_assessments/">server_vulnerability_assessments</a><br />
<a href="/providers/azure/sql/servers/">servers</a><br />
<a href="/providers/azure/sql/service_objectives/">service_objectives</a><br />
<a href="/providers/azure/sql/subscription_usages/">subscription_usages</a><br />
<a href="/providers/azure/sql/synapse_link_workspaces/">synapse_link_workspaces</a><br />
<a href="/providers/azure/sql/sync_agents/">sync_agents</a><br />
<a href="/providers/azure/sql/sync_groups/">sync_groups</a><br />
<a href="/providers/azure/sql/sync_members/">sync_members</a><br />
<a href="/providers/azure/sql/tde_certificates/">tde_certificates</a><br />
<a href="/providers/azure/sql/time_zones/">time_zones</a><br />
<a href="/providers/azure/sql/transparent_data_encryptions/">transparent_data_encryptions</a><br />
<a href="/providers/azure/sql/usages/">usages</a><br />
<a href="/providers/azure/sql/virtual_clusters/">virtual_clusters</a><br />
<a href="/providers/azure/sql/virtual_network_rules/">virtual_network_rules</a><br />
<a href="/providers/azure/sql/vulnerability_assessment_baseline/">vulnerability_assessment_baseline</a><br />
<a href="/providers/azure/sql/vulnerability_assessment_baselines/">vulnerability_assessment_baselines</a><br />
<a href="/providers/azure/sql/vulnerability_assessment_execute_scan/">vulnerability_assessment_execute_scan</a><br />
<a href="/providers/azure/sql/vulnerability_assessment_rule_baseline/">vulnerability_assessment_rule_baseline</a><br />
<a href="/providers/azure/sql/vulnerability_assessment_rule_baselines/">vulnerability_assessment_rule_baselines</a><br />
<a href="/providers/azure/sql/vulnerability_assessment_scan_result/">vulnerability_assessment_scan_result</a><br />
<a href="/providers/azure/sql/vulnerability_assessment_scans/">vulnerability_assessment_scans</a><br />
<a href="/providers/azure/sql/vulnerability_assessments/">vulnerability_assessments</a><br />
<a href="/providers/azure/sql/vulnerability_assessments_settings/">vulnerability_assessments_settings</a><br />
<a href="/providers/azure/sql/workload_classifiers/">workload_classifiers</a><br />
<a href="/providers/azure/sql/workload_groups/">workload_groups</a><br />
</div>
</div>

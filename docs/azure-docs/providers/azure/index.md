---
title: azure
hide_title: false
hide_table_of_contents: false
keywords:
  - azure
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
 Cloud computing services operated by Microsoft.  
    

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation
```bash
REGISTRY PULL azure v0.3.0;
```

## Authentication
```javascript

{
  "azure": {
    /**
      * Type of authentication to use, suported values include: api_key
      * @type String
      */
    "type": string, 
    /**
      * Environment variable name containing the api token obtained using the azure cli or SDK.
      * @type String
      */
    "credentialsenvvar": string, 
    /**
      * Value prepended to the request header, e.g. "Bearer "
      * Must be set to "Bearer "
      * @type String
      */
    "valuePrefix": string, 
  }
}

```
### Example (Mac/Linux)
```bash

AZ_ACCESS_TOKEN_RAW=$(az account get-access-token --query accessToken --output tsv)
export AZ_ACCESS_TOKEN=`echo $AZ_ACCESS_TOKEN_RAW | tr -d '\r'`
AUTH='{ "azure": { "type": "api_key", "valuePrefix": "Bearer ", "credentialsenvvar": "AZ_ACCESS_TOKEN" } }'
stackql shell --auth="${AUTH}"

```
### Example (PowerShell)
```powershell

$Env:AZ_ACCESS_TOKEN = "$(az account get-access-token --query accessToken --output tsv)".Trim("`r")
$Auth = "{ 'azure': { 'type': 'api_key', 'valuePrefix': 'Bearer ', 'credentialsenvvar': 'AZ_ACCESS_TOKEN' } }"
stackql.exe shell --auth=$Auth

```
## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure/aad_domain_services/">aad_domain_services</a><br />
<a href="/providers/azure/analysis_services/">analysis_services</a><br />
<a href="/providers/azure/api_management/">api_management</a><br />
<a href="/providers/azure/app_configuration/">app_configuration</a><br />
<a href="/providers/azure/application_insights/">application_insights</a><br />
<a href="/providers/azure/attestation/">attestation</a><br />
<a href="/providers/azure/authorization/">authorization</a><br />
<a href="/providers/azure/azure_active_directory/">azure_active_directory</a><br />
<a href="/providers/azure/azure_stack_hci/">azure_stack_hci</a><br />
<a href="/providers/azure/backup_admin/">backup_admin</a><br />
<a href="/providers/azure/bare_metal_infrastructure/">bare_metal_infrastructure</a><br />
<a href="/providers/azure/batch/">batch</a><br />
<a href="/providers/azure/billing/">billing</a><br />
<a href="/providers/azure/blueprint/">blueprint</a><br />
<a href="/providers/azure/cdn/">cdn</a><br />
<a href="/providers/azure/cloud_shell/">cloud_shell</a><br />
<a href="/providers/azure/cognitive_services/">cognitive_services</a><br />
<a href="/providers/azure/compute/">compute</a><br />
<a href="/providers/azure/compute_admin/">compute_admin</a><br />
<a href="/providers/azure/confluent/">confluent</a><br />
<a href="/providers/azure/consumption/">consumption</a><br />
<a href="/providers/azure/container_apps/">container_apps</a><br />
<a href="/providers/azure/container_instance/">container_instance</a><br />
<a href="/providers/azure/container_registry/">container_registry</a><br />
<a href="/providers/azure/container_registry_admin/">container_registry_admin</a><br />
<a href="/providers/azure/container_service/">container_service</a><br />
<a href="/providers/azure/container_service_admin/">container_service_admin</a><br />
<a href="/providers/azure/cosmos_db/">cosmos_db</a><br />
<a href="/providers/azure/cost_management/">cost_management</a><br />
<a href="/providers/azure/data_catalog/">data_catalog</a><br />
<a href="/providers/azure/data_factory/">data_factory</a><br />
<a href="/providers/azure/data_lake_analytics/">data_lake_analytics</a><br />
<a href="/providers/azure/data_lake_store/">data_lake_store</a><br />
<a href="/providers/azure/data_migration/">data_migration</a><br />
<a href="/providers/azure/data_protection/">data_protection</a><br />
<a href="/providers/azure/databricks/">databricks</a><br />
<a href="/providers/azure/datadog/">datadog</a><br />
<a href="/providers/azure/deployment_admin/">deployment_admin</a><br />
<a href="/providers/azure/deployment_manager/">deployment_manager</a><br />
<a href="/providers/azure/devops/">devops</a><br />
<a href="/providers/azure/dns/">dns</a><br />
<a href="/providers/azure/dns_resolver/">dns_resolver</a><br />
<a href="/providers/azure/dynatrace/">dynatrace</a><br />
<a href="/providers/azure/enterprise_knowledge_graph/">enterprise_knowledge_graph</a><br />
<a href="/providers/azure/event_grid/">event_grid</a><br />
<a href="/providers/azure/event_hub/">event_hub</a><br />
<a href="/providers/azure/guest_configuration/">guest_configuration</a><br />
<a href="/providers/azure/hardware_security_modules/">hardware_security_modules</a><br />
<a href="/providers/azure/hdinsight/">hdinsight</a><br />
<a href="/providers/azure/hybrid_aks/">hybrid_aks</a><br />
<a href="/providers/azure/hybrid_compute/">hybrid_compute</a><br />
<a href="/providers/azure/hybrid_connectivity/">hybrid_connectivity</a><br />
<a href="/providers/azure/hybrid_data_manager/">hybrid_data_manager</a><br />
<a href="/providers/azure/hybrid_kubernetes/">hybrid_kubernetes</a><br />
<a href="/providers/azure/hybrid_network/">hybrid_network</a><br />
<a href="/providers/azure/infrastructure_insights/">infrastructure_insights</a><br />
<a href="/providers/azure/iot_central/">iot_central</a><br />
<a href="/providers/azure/iot_hub/">iot_hub</a><br />
<a href="/providers/azure/iot_security/">iot_security</a><br />
<a href="/providers/azure/key_vault/">key_vault</a><br />
<a href="/providers/azure/key_vault_admin/">key_vault_admin</a><br />
<a href="/providers/azure/kubernetes_configuration/">kubernetes_configuration</a><br />
<a href="/providers/azure/logic_apps/">logic_apps</a><br />
<a href="/providers/azure/logz/">logz</a><br />
<a href="/providers/azure/machine_learning/">machine_learning</a><br />
<a href="/providers/azure/machine_learning_compute/">machine_learning_compute</a><br />
<a href="/providers/azure/machine_learning_experimentation/">machine_learning_experimentation</a><br />
<a href="/providers/azure/machine_learning_services/">machine_learning_services</a><br />
<a href="/providers/azure/maintenance/">maintenance</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure/managed_network/">managed_network</a><br />
<a href="/providers/azure/managed_service_identity/">managed_service_identity</a><br />
<a href="/providers/azure/managed_services/">managed_services</a><br />
<a href="/providers/azure/management_groups/">management_groups</a><br />
<a href="/providers/azure/maria_db/">maria_db</a><br />
<a href="/providers/azure/monitor/">monitor</a><br />
<a href="/providers/azure/mysql/">mysql</a><br />
<a href="/providers/azure/netapp/">netapp</a><br />
<a href="/providers/azure/network/">network</a><br />
<a href="/providers/azure/network_admin/">network_admin</a><br />
<a href="/providers/azure/network_function/">network_function</a><br />
<a href="/providers/azure/notification_hubs/">notification_hubs</a><br />
<a href="/providers/azure/operational_insights/">operational_insights</a><br />
<a href="/providers/azure/operations_management/">operations_management</a><br />
<a href="/providers/azure/peering/">peering</a><br />
<a href="/providers/azure/portal/">portal</a><br />
<a href="/providers/azure/postgresql/">postgresql</a><br />
<a href="/providers/azure/postgresql_hsc/">postgresql_hsc</a><br />
<a href="/providers/azure/power_platform/">power_platform</a><br />
<a href="/providers/azure/powerbi_dedicated/">powerbi_dedicated</a><br />
<a href="/providers/azure/powerbi_embedded/">powerbi_embedded</a><br />
<a href="/providers/azure/powerbi_privatelinks/">powerbi_privatelinks</a><br />
<a href="/providers/azure/private_dns/">private_dns</a><br />
<a href="/providers/azure/provider_hub/">provider_hub</a><br />
<a href="/providers/azure/purview/">purview</a><br />
<a href="/providers/azure/recovery_services/">recovery_services</a><br />
<a href="/providers/azure/recovery_services_backup/">recovery_services_backup</a><br />
<a href="/providers/azure/recovery_services_site_recovery/">recovery_services_site_recovery</a><br />
<a href="/providers/azure/redhat_openshift/">redhat_openshift</a><br />
<a href="/providers/azure/redis/">redis</a><br />
<a href="/providers/azure/redis_enterprise/">redis_enterprise</a><br />
<a href="/providers/azure/reservations/">reservations</a><br />
<a href="/providers/azure/resource_connector/">resource_connector</a><br />
<a href="/providers/azure/resource_graph/">resource_graph</a><br />
<a href="/providers/azure/resource_health/">resource_health</a><br />
<a href="/providers/azure/resource_mover/">resource_mover</a><br />
<a href="/providers/azure/resources/">resources</a><br />
<a href="/providers/azure/scheduler/">scheduler</a><br />
<a href="/providers/azure/security/">security</a><br />
<a href="/providers/azure/security_and_compliance/">security_and_compliance</a><br />
<a href="/providers/azure/security_insights/">security_insights</a><br />
<a href="/providers/azure/serial_console/">serial_console</a><br />
<a href="/providers/azure/service_bus/">service_bus</a><br />
<a href="/providers/azure/service_fabric/">service_fabric</a><br />
<a href="/providers/azure/service_fabric_managed_clusters/">service_fabric_managed_clusters</a><br />
<a href="/providers/azure/service_fabric_mesh/">service_fabric_mesh</a><br />
<a href="/providers/azure/service_linker/">service_linker</a><br />
<a href="/providers/azure/service_map/">service_map</a><br />
<a href="/providers/azure/softwareplan/">softwareplan</a><br />
<a href="/providers/azure/sql/">sql</a><br />
<a href="/providers/azure/sql_virtual_machine/">sql_virtual_machine</a><br />
<a href="/providers/azure/storage/">storage</a><br />
<a href="/providers/azure/storage_admin/">storage_admin</a><br />
<a href="/providers/azure/storage_cache/">storage_cache</a><br />
<a href="/providers/azure/storage_import_export/">storage_import_export</a><br />
<a href="/providers/azure/storage_mover/">storage_mover</a><br />
<a href="/providers/azure/storage_pool/">storage_pool</a><br />
<a href="/providers/azure/storage_sync/">storage_sync</a><br />
<a href="/providers/azure/stream_analytics/">stream_analytics</a><br />
<a href="/providers/azure/subscription/">subscription</a><br />
<a href="/providers/azure/subscriptions_admin/">subscriptions_admin</a><br />
<a href="/providers/azure/support/">support</a><br />
<a href="/providers/azure/synapse/">synapse</a><br />
<a href="/providers/azure/system_center_vm_manager/">system_center_vm_manager</a><br />
<a href="/providers/azure/time_series_insights/">time_series_insights</a><br />
<a href="/providers/azure/traffic_manager/">traffic_manager</a><br />
<a href="/providers/azure/virtual_machine_images/">virtual_machine_images</a><br />
<a href="/providers/azure/web_apps/">web_apps</a><br />
<a href="/providers/azure/web_pub_sub/">web_pub_sub</a><br />
</div>
</div>

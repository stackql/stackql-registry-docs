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
id: azure-doc
slug: /providers/azure
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Cloud computing services operated by Microsoft.  
    
:::info Provider Summary (v24.06.00242)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>196</b></span><br />
<span>total methods:&nbsp;<b>11160</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>4020</b></span><br />
<span>total selectable resources:&nbsp;<b>3581</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `azure` provider, run the following command:  

```bash
REGISTRY PULL azure;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication

StackQL uses Azure application credentials obtained using the <CopyableCode code="az login" /> command from the Azure SDK.  For more information, see <a href="https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli">here</a>.

### Authenticating using an Azure Service Principal

To authenticate using an Azure Service Principal, set the following environment variables: <CopyableCode code="AZURE_TENANT_ID" />, <CopyableCode code="AZURE_CLIENT_ID" /> and <CopyableCode code="AZURE_CLIENT_SECRET" />, see [__creating-an-azure-service-principal__](https://learn.microsoft.com/en-us/azure/developer/go/azure-sdk-authentication-service-principal?tabs=azure-cli#2-create-an-azure-service-principal).


## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure/aad_b2c/">aad_b2c</a><br />
<a href="/providers/azure/aad_domain_services/">aad_domain_services</a><br />
<a href="/providers/azure/ad_hybrid_health_service/">ad_hybrid_health_service</a><br />
<a href="/providers/azure/advisor/">advisor</a><br />
<a href="/providers/azure/aks/">aks</a><br />
<a href="/providers/azure/alerts_management/">alerts_management</a><br />
<a href="/providers/azure/analysis_services/">analysis_services</a><br />
<a href="/providers/azure/api_center/">api_center</a><br />
<a href="/providers/azure/api_management/">api_management</a><br />
<a href="/providers/azure/app_configuration/">app_configuration</a><br />
<a href="/providers/azure/app_service/">app_service</a><br />
<a href="/providers/azure/application_insights/">application_insights</a><br />
<a href="/providers/azure/attestation/">attestation</a><br />
<a href="/providers/azure/authorization/">authorization</a><br />
<a href="/providers/azure/automanage/">automanage</a><br />
<a href="/providers/azure/automation/">automation</a><br />
<a href="/providers/azure/autonomous_dev_platform/">autonomous_dev_platform</a><br />
<a href="/providers/azure/azure_active_directory/">azure_active_directory</a><br />
<a href="/providers/azure/azure_arc_data/">azure_arc_data</a><br />
<a href="/providers/azure/azure_data/">azure_data</a><br />
<a href="/providers/azure/azurefleet/">azurefleet</a><br />
<a href="/providers/azure/bare_metal_infrastructure/">bare_metal_infrastructure</a><br />
<a href="/providers/azure/batch/">batch</a><br />
<a href="/providers/azure/billing/">billing</a><br />
<a href="/providers/azure/billing_benefits/">billing_benefits</a><br />
<a href="/providers/azure/blueprints/">blueprints</a><br />
<a href="/providers/azure/bot_service/">bot_service</a><br />
<a href="/providers/azure/cdn/">cdn</a><br />
<a href="/providers/azure/change_analysis/">change_analysis</a><br />
<a href="/providers/azure/cloud_shell/">cloud_shell</a><br />
<a href="/providers/azure/cognitive_services/">cognitive_services</a><br />
<a href="/providers/azure/communication/">communication</a><br />
<a href="/providers/azure/compute/">compute</a><br />
<a href="/providers/azure/confidential_ledger/">confidential_ledger</a><br />
<a href="/providers/azure/consumption/">consumption</a><br />
<a href="/providers/azure/container_apps/">container_apps</a><br />
<a href="/providers/azure/container_instances/">container_instances</a><br />
<a href="/providers/azure/container_registry/">container_registry</a><br />
<a href="/providers/azure/container_storage/">container_storage</a><br />
<a href="/providers/azure/cosmos_db/">cosmos_db</a><br />
<a href="/providers/azure/cost_management/">cost_management</a><br />
<a href="/providers/azure/custom_locations/">custom_locations</a><br />
<a href="/providers/azure/custom_providers/">custom_providers</a><br />
<a href="/providers/azure/customer_lockbox/">customer_lockbox</a><br />
<a href="/providers/azure/dashboard/">dashboard</a><br />
<a href="/providers/azure/data_box/">data_box</a><br />
<a href="/providers/azure/data_box_edge/">data_box_edge</a><br />
<a href="/providers/azure/data_catalog/">data_catalog</a><br />
<a href="/providers/azure/data_explorer/">data_explorer</a><br />
<a href="/providers/azure/data_factory/">data_factory</a><br />
<a href="/providers/azure/data_lake_analytics/">data_lake_analytics</a><br />
<a href="/providers/azure/data_lake_store/">data_lake_store</a><br />
<a href="/providers/azure/data_migration/">data_migration</a><br />
<a href="/providers/azure/data_protection/">data_protection</a><br />
<a href="/providers/azure/data_replication/">data_replication</a><br />
<a href="/providers/azure/data_share/">data_share</a><br />
<a href="/providers/azure/data_transfer/">data_transfer</a><br />
<a href="/providers/azure/databasewatcher/">databasewatcher</a><br />
<a href="/providers/azure/defender/">defender</a><br />
<a href="/providers/azure/delegated_network/">delegated_network</a><br />
<a href="/providers/azure/desktop_virtualization/">desktop_virtualization</a><br />
<a href="/providers/azure/dev_center/">dev_center</a><br />
<a href="/providers/azure/dev_test_labs/">dev_test_labs</a><br />
<a href="/providers/azure/device_registry/">device_registry</a><br />
<a href="/providers/azure/device_update/">device_update</a><br />
<a href="/providers/azure/devops/">devops</a><br />
<a href="/providers/azure/devops_infrastructure/">devops_infrastructure</a><br />
<a href="/providers/azure/digital_twins/">digital_twins</a><br />
<a href="/providers/azure/dns/">dns</a><br />
<a href="/providers/azure/dns_resolver/">dns_resolver</a><br />
<a href="/providers/azure/edgezones/">edgezones</a><br />
<a href="/providers/azure/elastic_san/">elastic_san</a><br />
<a href="/providers/azure/engagement_fabric/">engagement_fabric</a><br />
<a href="/providers/azure/event_grid/">event_grid</a><br />
<a href="/providers/azure/event_hubs/">event_hubs</a><br />
<a href="/providers/azure/fleet/">fleet</a><br />
<a href="/providers/azure/fluid_relay/">fluid_relay</a><br />
<a href="/providers/azure/front_door/">front_door</a><br />
<a href="/providers/azure/graph_services/">graph_services</a><br />
<a href="/providers/azure/guest_configuration/">guest_configuration</a><br />
<a href="/providers/azure/hardware_security_modules/">hardware_security_modules</a><br />
<a href="/providers/azure/hdinsight/">hdinsight</a><br />
<a href="/providers/azure/hybrid_aks/">hybrid_aks</a><br />
<a href="/providers/azure/hybrid_cloud/">hybrid_cloud</a><br />
<a href="/providers/azure/hybrid_compute/">hybrid_compute</a><br />
<a href="/providers/azure/hybrid_connectivity/">hybrid_connectivity</a><br />
<a href="/providers/azure/hybrid_data_manager/">hybrid_data_manager</a><br />
<a href="/providers/azure/hybrid_kubernetes/">hybrid_kubernetes</a><br />
<a href="/providers/azure/hybrid_network/">hybrid_network</a><br />
<a href="/providers/azure/image_builder/">image_builder</a><br />
<a href="/providers/azure/integration_environment/">integration_environment</a><br />
<a href="/providers/azure/iot_central/">iot_central</a><br />
<a href="/providers/azure/iot_data_processor/">iot_data_processor</a><br />
<a href="/providers/azure/iot_firmware_defense/">iot_firmware_defense</a><br />
<a href="/providers/azure/iot_hub/">iot_hub</a><br />
<a href="/providers/azure/iot_hub_device_provisioning/">iot_hub_device_provisioning</a><br />
<a href="/providers/azure/iot_mq/">iot_mq</a><br />
<a href="/providers/azure/iot_orchestrator/">iot_orchestrator</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure/key_vault/">key_vault</a><br />
<a href="/providers/azure/kubernetes_configuration/">kubernetes_configuration</a><br />
<a href="/providers/azure/kubernetesruntime/">kubernetesruntime</a><br />
<a href="/providers/azure/lab_services/">lab_services</a><br />
<a href="/providers/azure/large_instances/">large_instances</a><br />
<a href="/providers/azure/load_testing/">load_testing</a><br />
<a href="/providers/azure/log_analytics/">log_analytics</a><br />
<a href="/providers/azure/logic_apps/">logic_apps</a><br />
<a href="/providers/azure/machine_learning/">machine_learning</a><br />
<a href="/providers/azure/maintenance/">maintenance</a><br />
<a href="/providers/azure/managed_applications/">managed_applications</a><br />
<a href="/providers/azure/managed_identity/">managed_identity</a><br />
<a href="/providers/azure/managed_network/">managed_network</a><br />
<a href="/providers/azure/managed_network_fabric/">managed_network_fabric</a><br />
<a href="/providers/azure/managed_services/">managed_services</a><br />
<a href="/providers/azure/management_groups/">management_groups</a><br />
<a href="/providers/azure/maps/">maps</a><br />
<a href="/providers/azure/maria_db/">maria_db</a><br />
<a href="/providers/azure/media_services/">media_services</a><br />
<a href="/providers/azure/migrate/">migrate</a><br />
<a href="/providers/azure/migrate_projects/">migrate_projects</a><br />
<a href="/providers/azure/mixed_reality/">mixed_reality</a><br />
<a href="/providers/azure/ml_services/">ml_services</a><br />
<a href="/providers/azure/mobile_network/">mobile_network</a><br />
<a href="/providers/azure/monitor/">monitor</a><br />
<a href="/providers/azure/mpc_network_function/">mpc_network_function</a><br />
<a href="/providers/azure/mysql/">mysql</a><br />
<a href="/providers/azure/network/">network</a><br />
<a href="/providers/azure/network_analytics/">network_analytics</a><br />
<a href="/providers/azure/network_function/">network_function</a><br />
<a href="/providers/azure/nexus/">nexus</a><br />
<a href="/providers/azure/notification_hubs/">notification_hubs</a><br />
<a href="/providers/azure/operations_management/">operations_management</a><br />
<a href="/providers/azure/orbital/">orbital</a><br />
<a href="/providers/azure/peering/">peering</a><br />
<a href="/providers/azure/playwrighttesting/">playwrighttesting</a><br />
<a href="/providers/azure/portal/">portal</a><br />
<a href="/providers/azure/portal_services/">portal_services</a><br />
<a href="/providers/azure/postgresql/">postgresql</a><br />
<a href="/providers/azure/postgresql_hsc/">postgresql_hsc</a><br />
<a href="/providers/azure/powerbi_dedicated/">powerbi_dedicated</a><br />
<a href="/providers/azure/powerbi_embedded/">powerbi_embedded</a><br />
<a href="/providers/azure/powerbi_privatelinks/">powerbi_privatelinks</a><br />
<a href="/providers/azure/private_dns/">private_dns</a><br />
<a href="/providers/azure/provider_hub/">provider_hub</a><br />
<a href="/providers/azure/purview/">purview</a><br />
<a href="/providers/azure/purview_policy/">purview_policy</a><br />
<a href="/providers/azure/quantum/">quantum</a><br />
<a href="/providers/azure/quota/">quota</a><br />
<a href="/providers/azure/recovery_services/">recovery_services</a><br />
<a href="/providers/azure/recovery_services_backup/">recovery_services_backup</a><br />
<a href="/providers/azure/recovery_services_site_recovery/">recovery_services_site_recovery</a><br />
<a href="/providers/azure/relay/">relay</a><br />
<a href="/providers/azure/reservations/">reservations</a><br />
<a href="/providers/azure/resource_connector/">resource_connector</a><br />
<a href="/providers/azure/resource_graph/">resource_graph</a><br />
<a href="/providers/azure/resource_mover/">resource_mover</a><br />
<a href="/providers/azure/resources/">resources</a><br />
<a href="/providers/azure/scheduler/">scheduler</a><br />
<a href="/providers/azure/scom/">scom</a><br />
<a href="/providers/azure/search/">search</a><br />
<a href="/providers/azure/security/">security</a><br />
<a href="/providers/azure/security_and_compliance/">security_and_compliance</a><br />
<a href="/providers/azure/security_devops/">security_devops</a><br />
<a href="/providers/azure/sentinel/">sentinel</a><br />
<a href="/providers/azure/serial_console/">serial_console</a><br />
<a href="/providers/azure/service_bus/">service_bus</a><br />
<a href="/providers/azure/service_connector/">service_connector</a><br />
<a href="/providers/azure/service_fabric/">service_fabric</a><br />
<a href="/providers/azure/service_fabric_managed_clusters/">service_fabric_managed_clusters</a><br />
<a href="/providers/azure/service_fabric_mesh/">service_fabric_mesh</a><br />
<a href="/providers/azure/service_networking/">service_networking</a><br />
<a href="/providers/azure/signalr/">signalr</a><br />
<a href="/providers/azure/software_plan/">software_plan</a><br />
<a href="/providers/azure/sphere/">sphere</a><br />
<a href="/providers/azure/spring_apps/">spring_apps</a><br />
<a href="/providers/azure/sql/">sql</a><br />
<a href="/providers/azure/sql_vm/">sql_vm</a><br />
<a href="/providers/azure/standbypool/">standbypool</a><br />
<a href="/providers/azure/storage/">storage</a><br />
<a href="/providers/azure/storage_cache/">storage_cache</a><br />
<a href="/providers/azure/storage_import_export/">storage_import_export</a><br />
<a href="/providers/azure/storage_mover/">storage_mover</a><br />
<a href="/providers/azure/storage_pool/">storage_pool</a><br />
<a href="/providers/azure/storage_sync/">storage_sync</a><br />
<a href="/providers/azure/storageactions/">storageactions</a><br />
<a href="/providers/azure/stream_analytics/">stream_analytics</a><br />
<a href="/providers/azure/subscription/">subscription</a><br />
<a href="/providers/azure/support/">support</a><br />
<a href="/providers/azure/synapse/">synapse</a><br />
<a href="/providers/azure/system_center_vm_manager/">system_center_vm_manager</a><br />
<a href="/providers/azure/time_series_insights/">time_series_insights</a><br />
<a href="/providers/azure/traffic_manager/">traffic_manager</a><br />
<a href="/providers/azure/verifiedid/">verifiedid</a><br />
<a href="/providers/azure/video_analyzer/">video_analyzer</a><br />
<a href="/providers/azure/voice_services/">voice_services</a><br />
<a href="/providers/azure/web_pubsub/">web_pubsub</a><br />
<a href="/providers/azure/workload_monitor/">workload_monitor</a><br />
</div>
</div>

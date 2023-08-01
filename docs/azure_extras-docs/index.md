---
title: azure_extras
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_extras
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
id: azure_extras-doc
slug: /providers/azure_extras

---
 Additional Azure cloud computing services by Microsoft.  
    
:::info Provider Summary (v23.03.00121)

<div class="row">
<div class="providerDocColumn">
<span>total services:&nbsp;<b>93</b></span><br />
<span>total methods:&nbsp;<b>2882</b></span><br />
</div>
<div class="providerDocColumn">
<span>total resources:&nbsp;<b>720</b></span><br />
<span>total selectable resources:&nbsp;<b>640</b></span><br />
</div>
</div>

:::

See also:   
[[` SHOW `]](https://stackql.io/docs/language-spec/show) [[` DESCRIBE `]](https://stackql.io/docs/language-spec/describe)  [[` REGISTRY `]](https://stackql.io/docs/language-spec/registry)
* * * 

## Installation

To pull the latest version of the `azure_extras` provider, run the following command:  

```bash
REGISTRY PULL azure_extras;
```
> To view previous provider versions or to pull a specific provider version, see [here](https://stackql.io/docs/language-spec/registry).  

## Authentication


StackQL uses Azure application credentials obtained using the `az login` command from the Azure SDK.  For more information, see [here](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).

## Services
<div class="row">
<div class="providerDocColumn">
<a href="/providers/azure_extras/ad_hybrid_health_service/">ad_hybrid_health_service</a><br />
<a href="/providers/azure_extras/addons/">addons</a><br />
<a href="/providers/azure_extras/advisor/">advisor</a><br />
<a href="/providers/azure_extras/ag_food_platform/">ag_food_platform</a><br />
<a href="/providers/azure_extras/alerts_management/">alerts_management</a><br />
<a href="/providers/azure_extras/app_platform/">app_platform</a><br />
<a href="/providers/azure_extras/automanage/">automanage</a><br />
<a href="/providers/azure_extras/automation/">automation</a><br />
<a href="/providers/azure_extras/autonomous_dev_platform/">autonomous_dev_platform</a><br />
<a href="/providers/azure_extras/azure_arc_data/">azure_arc_data</a><br />
<a href="/providers/azure_extras/azure_bridge_admin/">azure_bridge_admin</a><br />
<a href="/providers/azure_extras/azure_data/">azure_data</a><br />
<a href="/providers/azure_extras/azure_stack/">azure_stack</a><br />
<a href="/providers/azure_extras/blockchain/">blockchain</a><br />
<a href="/providers/azure_extras/bot_service/">bot_service</a><br />
<a href="/providers/azure_extras/change_analysis/">change_analysis</a><br />
<a href="/providers/azure_extras/chaos/">chaos</a><br />
<a href="/providers/azure_extras/commerce/">commerce</a><br />
<a href="/providers/azure_extras/commerce_admin/">commerce_admin</a><br />
<a href="/providers/azure_extras/communication/">communication</a><br />
<a href="/providers/azure_extras/confidential_ledger/">confidential_ledger</a><br />
<a href="/providers/azure_extras/connected_vsphere/">connected_vsphere</a><br />
<a href="/providers/azure_extras/custom_locations/">custom_locations</a><br />
<a href="/providers/azure_extras/custom_providers/">custom_providers</a><br />
<a href="/providers/azure_extras/customer_insights/">customer_insights</a><br />
<a href="/providers/azure_extras/customer_lockbox/">customer_lockbox</a><br />
<a href="/providers/azure_extras/dashboard/">dashboard</a><br />
<a href="/providers/azure_extras/data_box/">data_box</a><br />
<a href="/providers/azure_extras/data_box_edge/">data_box_edge</a><br />
<a href="/providers/azure_extras/data_share/">data_share</a><br />
<a href="/providers/azure_extras/delegated_network/">delegated_network</a><br />
<a href="/providers/azure_extras/desktop_virtualization/">desktop_virtualization</a><br />
<a href="/providers/azure_extras/dev_center/">dev_center</a><br />
<a href="/providers/azure_extras/dev_hub/">dev_hub</a><br />
<a href="/providers/azure_extras/dev_spaces/">dev_spaces</a><br />
<a href="/providers/azure_extras/dev_test_labs/">dev_test_labs</a><br />
<a href="/providers/azure_extras/device_update/">device_update</a><br />
<a href="/providers/azure_extras/devices/">devices</a><br />
<a href="/providers/azure_extras/digital_twins/">digital_twins</a><br />
<a href="/providers/azure_extras/dyn365_fraud_protection/">dyn365_fraud_protection</a><br />
<a href="/providers/azure_extras/edge_order/">edge_order</a><br />
<a href="/providers/azure_extras/edge_order_partner/">edge_order_partner</a><br />
<a href="/providers/azure_extras/education/">education</a><br />
<a href="/providers/azure_extras/elastic/">elastic</a><br />
<a href="/providers/azure_extras/elastic_san/">elastic_san</a><br />
<a href="/providers/azure_extras/engagement_fabric/">engagement_fabric</a><br />
<a href="/providers/azure_extras/external_identities/">external_identities</a><br />
</div>
<div class="providerDocColumn">
<a href="/providers/azure_extras/fabric_admin/">fabric_admin</a><br />
<a href="/providers/azure_extras/fluid_relay/">fluid_relay</a><br />
<a href="/providers/azure_extras/front_door/">front_door</a><br />
<a href="/providers/azure_extras/gallery_admin/">gallery_admin</a><br />
<a href="/providers/azure_extras/hana_on_azure/">hana_on_azure</a><br />
<a href="/providers/azure_extras/health_bot/">health_bot</a><br />
<a href="/providers/azure_extras/healthcare_apis/">healthcare_apis</a><br />
<a href="/providers/azure_extras/intune/">intune</a><br />
<a href="/providers/azure_extras/kusto/">kusto</a><br />
<a href="/providers/azure_extras/lab_services/">lab_services</a><br />
<a href="/providers/azure_extras/load_test_service/">load_test_service</a><br />
<a href="/providers/azure_extras/m365_security_and_compliance/">m365_security_and_compliance</a><br />
<a href="/providers/azure_extras/management_partner/">management_partner</a><br />
<a href="/providers/azure_extras/maps/">maps</a><br />
<a href="/providers/azure_extras/marketplace/">marketplace</a><br />
<a href="/providers/azure_extras/marketplace_catalog/">marketplace_catalog</a><br />
<a href="/providers/azure_extras/marketplace_notifications/">marketplace_notifications</a><br />
<a href="/providers/azure_extras/marketplace_ordering/">marketplace_ordering</a><br />
<a href="/providers/azure_extras/media_services/">media_services</a><br />
<a href="/providers/azure_extras/migrate/">migrate</a><br />
<a href="/providers/azure_extras/migrate_projects/">migrate_projects</a><br />
<a href="/providers/azure_extras/mixed_reality/">mixed_reality</a><br />
<a href="/providers/azure_extras/mobile_network/">mobile_network</a><br />
<a href="/providers/azure_extras/nginx/">nginx</a><br />
<a href="/providers/azure_extras/open_energy_platform/">open_energy_platform</a><br />
<a href="/providers/azure_extras/orbital/">orbital</a><br />
<a href="/providers/azure_extras/quantum/">quantum</a><br />
<a href="/providers/azure_extras/quota/">quota</a><br />
<a href="/providers/azure_extras/recommendations_service/">recommendations_service</a><br />
<a href="/providers/azure_extras/relay/">relay</a><br />
<a href="/providers/azure_extras/saas/">saas</a><br />
<a href="/providers/azure_extras/search/">search</a><br />
<a href="/providers/azure_extras/signalr/">signalr</a><br />
<a href="/providers/azure_extras/solutions/">solutions</a><br />
<a href="/providers/azure_extras/stor_simple_8000_series/">stor_simple_8000_series</a><br />
<a href="/providers/azure_extras/test_base/">test_base</a><br />
<a href="/providers/azure_extras/update_admin/">update_admin</a><br />
<a href="/providers/azure_extras/video_analyzer/">video_analyzer</a><br />
<a href="/providers/azure_extras/video_indexer/">video_indexer</a><br />
<a href="/providers/azure_extras/visual_studio/">visual_studio</a><br />
<a href="/providers/azure_extras/vmware/">vmware</a><br />
<a href="/providers/azure_extras/vmware_cloud_simple/">vmware_cloud_simple</a><br />
<a href="/providers/azure_extras/windows_extended_security_updates/">windows_extended_security_updates</a><br />
<a href="/providers/azure_extras/windows_iot/">windows_iot</a><br />
<a href="/providers/azure_extras/workload_monitor/">workload_monitor</a><br />
<a href="/providers/azure_extras/workloads/">workloads</a><br />
</div>
</div>
---
title: web_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps
  - app_service
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `extendedLocation` | `object` | Extended Location. |
| `identity` | `object` | Managed service identity. |
| `properties` | `object` | Site resource specific properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the details of a web, mobile, or API app. |
| `list` | `SELECT` | `subscriptionId` | Description for Get all apps for a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Gets all web, mobile, and API apps in the specified resource group. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Deletes a web, mobile, or API app, or one of the deployment slots. |
| `_list` | `EXEC` | `subscriptionId` | Description for Get all apps for a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Gets all web, mobile, and API apps in the specified resource group. |
| `add_premier_add_on` | `EXEC` | `name, premierAddOnName, resourceGroupName, subscriptionId` | Description for Updates a named add-on of an app. |
| `add_premier_add_on_slot` | `EXEC` | `name, premierAddOnName, resourceGroupName, slot, subscriptionId` | Description for Updates a named add-on of an app. |
| `analyze_custom_hostname` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Analyze a custom hostname. |
| `analyze_custom_hostname_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Analyze a custom hostname. |
| `apply_slot_config_to_production` | `EXEC` | `name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Applies the configuration settings from the target slot onto the current slot. |
| `apply_slot_configuration_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Applies the configuration settings from the target slot onto the current slot. |
| `approve_or_reject_private_endpoint_connection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `approve_or_reject_private_endpoint_connection_slot` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, slot, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `backup` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates a backup of an app. |
| `backup_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Creates a backup of an app. |
| `deploy_workflow_artifacts` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates the artifacts for web site, or a deployment slot. |
| `deploy_workflow_artifacts_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Creates the artifacts for web site, or a deployment slot. |
| `discover_backup` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. |
| `discover_backup_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. |
| `generate_new_site_publishing_password` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Generates a new publishing password for an app (or deployment slot, if specified). |
| `generate_new_site_publishing_password_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Generates a new publishing password for an app (or deployment slot, if specified). |
| `install_site_extension` | `EXEC` | `name, resourceGroupName, siteExtensionId, subscriptionId` | Description for Install site extension on a web site, or a deployment slot. |
| `install_site_extension_slot` | `EXEC` | `name, resourceGroupName, siteExtensionId, slot, subscriptionId` | Description for Install site extension on a web site, or a deployment slot. |
| `is_cloneable` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Shows whether an app can be cloned to another resource group or subscription. |
| `is_cloneable_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Shows whether an app can be cloned to another resource group or subscription. |
| `migrate_my_sql` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Migrates a local (in-app) MySql database to a remote MySql database. |
| `migrate_storage` | `EXEC` | `name, resourceGroupName, subscriptionId, subscriptionName` | Description for Restores a web app. |
| `put_private_access_vnet` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site. |
| `put_private_access_vnet_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site. |
| `recover_site_configuration_snapshot` | `EXEC` | `name, resourceGroupName, snapshotId, subscriptionId` | Description for Reverts the configuration of an app to a previous snapshot. |
| `recover_site_configuration_snapshot_slot` | `EXEC` | `name, resourceGroupName, slot, snapshotId, subscriptionId` | Description for Reverts the configuration of an app to a previous snapshot. |
| `reset_production_slot_config` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. |
| `reset_slot_configuration_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. |
| `restart` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restarts an app (or deployment slot, if specified). |
| `restart_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restarts an app (or deployment slot, if specified). |
| `restore` | `EXEC` | `backupId, name, resourceGroupName, subscriptionId` | Description for Restores a specific backup to another app (or deployment slot, if specified). |
| `restore_from_backup_blob` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restores an app from a backup blob in Azure Storage. |
| `restore_from_backup_blob_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restores an app from a backup blob in Azure Storage. |
| `restore_from_deleted_app` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restores a deleted web app to this web app. |
| `restore_from_deleted_app_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restores a deleted web app to this web app. |
| `restore_slot` | `EXEC` | `backupId, name, resourceGroupName, slot, subscriptionId` | Description for Restores a specific backup to another app (or deployment slot, if specified). |
| `restore_snapshot` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restores a web app from a snapshot. |
| `restore_snapshot_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restores a web app from a snapshot. |
| `run_triggered_web_job` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Run a triggered web job for an app, or a deployment slot. |
| `run_triggered_web_job_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Run a triggered web job for an app, or a deployment slot. |
| `start` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Starts an app (or deployment slot, if specified). |
| `start_continuous_web_job` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Start a continuous web job for an app, or a deployment slot. |
| `start_continuous_web_job_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Start a continuous web job for an app, or a deployment slot. |
| `start_network_trace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Start capturing network packets for the site. |
| `start_network_trace_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Start capturing network packets for the site. |
| `start_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Starts an app (or deployment slot, if specified). |
| `start_web_site_network_trace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Start capturing network packets for the site (To be deprecated). |
| `start_web_site_network_trace_operation` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Start capturing network packets for the site. |
| `start_web_site_network_trace_operation_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Start capturing network packets for the site. |
| `start_web_site_network_trace_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Start capturing network packets for the site (To be deprecated). |
| `stop` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Stops an app (or deployment slot, if specified). |
| `stop_continuous_web_job` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Stop a continuous web job for an app, or a deployment slot. |
| `stop_continuous_web_job_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Stop a continuous web job for an app, or a deployment slot. |
| `stop_network_trace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `stop_network_trace_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `stop_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Stops an app (or deployment slot, if specified). |
| `stop_web_site_network_trace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `stop_web_site_network_trace_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `swap_slot_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Swaps two deployment slots of an app. |
| `swap_slot_with_production` | `EXEC` | `name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Swaps two deployment slots of an app. |
| `sync_function_triggers` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `sync_function_triggers_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `sync_functions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `sync_functions_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `sync_repository` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Sync web app repository. |
| `sync_repository_slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Sync web app repository. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |

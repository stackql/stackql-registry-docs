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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="extendedLocation" /> | `object` | Extended Location. |
| <CopyableCode code="identity" /> | `object` | Managed service identity. |
| <CopyableCode code="properties" /> | `object` | Site resource specific properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the details of a web, mobile, or API app. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all apps for a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Gets all web, mobile, and API apps in the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Deletes a web, mobile, or API app, or one of the deployment slots. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Get all apps for a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Gets all web, mobile, and API apps in the specified resource group. |
| <CopyableCode code="add_premier_add_on" /> | `EXEC` | <CopyableCode code="name, premierAddOnName, resourceGroupName, subscriptionId" /> | Description for Updates a named add-on of an app. |
| <CopyableCode code="add_premier_add_on_slot" /> | `EXEC` | <CopyableCode code="name, premierAddOnName, resourceGroupName, slot, subscriptionId" /> | Description for Updates a named add-on of an app. |
| <CopyableCode code="analyze_custom_hostname" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Analyze a custom hostname. |
| <CopyableCode code="analyze_custom_hostname_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Analyze a custom hostname. |
| <CopyableCode code="apply_slot_config_to_production" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot" /> | Description for Applies the configuration settings from the target slot onto the current slot. |
| <CopyableCode code="apply_slot_configuration_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, data__preserveVnet, data__targetSlot" /> | Description for Applies the configuration settings from the target slot onto the current slot. |
| <CopyableCode code="approve_or_reject_private_endpoint_connection" /> | `EXEC` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Description for Approves or rejects a private endpoint connection |
| <CopyableCode code="approve_or_reject_private_endpoint_connection_slot" /> | `EXEC` | <CopyableCode code="name, privateEndpointConnectionName, resourceGroupName, slot, subscriptionId" /> | Description for Approves or rejects a private endpoint connection |
| <CopyableCode code="backup" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates a backup of an app. |
| <CopyableCode code="backup_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Creates a backup of an app. |
| <CopyableCode code="deploy_workflow_artifacts" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates the artifacts for web site, or a deployment slot. |
| <CopyableCode code="deploy_workflow_artifacts_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Creates the artifacts for web site, or a deployment slot. |
| <CopyableCode code="discover_backup" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. |
| <CopyableCode code="discover_backup_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. |
| <CopyableCode code="generate_new_site_publishing_password" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Generates a new publishing password for an app (or deployment slot, if specified). |
| <CopyableCode code="generate_new_site_publishing_password_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Generates a new publishing password for an app (or deployment slot, if specified). |
| <CopyableCode code="install_site_extension" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, siteExtensionId, subscriptionId" /> | Description for Install site extension on a web site, or a deployment slot. |
| <CopyableCode code="install_site_extension_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, siteExtensionId, slot, subscriptionId" /> | Description for Install site extension on a web site, or a deployment slot. |
| <CopyableCode code="is_cloneable" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Shows whether an app can be cloned to another resource group or subscription. |
| <CopyableCode code="is_cloneable_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Shows whether an app can be cloned to another resource group or subscription. |
| <CopyableCode code="migrate_my_sql" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Migrates a local (in-app) MySql database to a remote MySql database. |
| <CopyableCode code="migrate_storage" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, subscriptionName" /> | Description for Restores a web app. |
| <CopyableCode code="put_private_access_vnet" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site. |
| <CopyableCode code="put_private_access_vnet_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site. |
| <CopyableCode code="recover_site_configuration_snapshot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, snapshotId, subscriptionId" /> | Description for Reverts the configuration of an app to a previous snapshot. |
| <CopyableCode code="recover_site_configuration_snapshot_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, snapshotId, subscriptionId" /> | Description for Reverts the configuration of an app to a previous snapshot. |
| <CopyableCode code="reset_production_slot_config" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. |
| <CopyableCode code="reset_slot_configuration_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Restarts an app (or deployment slot, if specified). |
| <CopyableCode code="restart_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Restarts an app (or deployment slot, if specified). |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="backupId, name, resourceGroupName, subscriptionId" /> | Description for Restores a specific backup to another app (or deployment slot, if specified). |
| <CopyableCode code="restore_from_backup_blob" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Restores an app from a backup blob in Azure Storage. |
| <CopyableCode code="restore_from_backup_blob_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Restores an app from a backup blob in Azure Storage. |
| <CopyableCode code="restore_from_deleted_app" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Restores a deleted web app to this web app. |
| <CopyableCode code="restore_from_deleted_app_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Restores a deleted web app to this web app. |
| <CopyableCode code="restore_slot" /> | `EXEC` | <CopyableCode code="backupId, name, resourceGroupName, slot, subscriptionId" /> | Description for Restores a specific backup to another app (or deployment slot, if specified). |
| <CopyableCode code="restore_snapshot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Restores a web app from a snapshot. |
| <CopyableCode code="restore_snapshot_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Restores a web app from a snapshot. |
| <CopyableCode code="run_triggered_web_job" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, webJobName" /> | Description for Run a triggered web job for an app, or a deployment slot. |
| <CopyableCode code="run_triggered_web_job_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, webJobName" /> | Description for Run a triggered web job for an app, or a deployment slot. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Starts an app (or deployment slot, if specified). |
| <CopyableCode code="start_continuous_web_job" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, webJobName" /> | Description for Start a continuous web job for an app, or a deployment slot. |
| <CopyableCode code="start_continuous_web_job_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, webJobName" /> | Description for Start a continuous web job for an app, or a deployment slot. |
| <CopyableCode code="start_network_trace" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Start capturing network packets for the site. |
| <CopyableCode code="start_network_trace_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Start capturing network packets for the site. |
| <CopyableCode code="start_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Starts an app (or deployment slot, if specified). |
| <CopyableCode code="start_web_site_network_trace" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Start capturing network packets for the site (To be deprecated). |
| <CopyableCode code="start_web_site_network_trace_operation" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Start capturing network packets for the site. |
| <CopyableCode code="start_web_site_network_trace_operation_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Start capturing network packets for the site. |
| <CopyableCode code="start_web_site_network_trace_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Start capturing network packets for the site (To be deprecated). |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Stops an app (or deployment slot, if specified). |
| <CopyableCode code="stop_continuous_web_job" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, webJobName" /> | Description for Stop a continuous web job for an app, or a deployment slot. |
| <CopyableCode code="stop_continuous_web_job_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, webJobName" /> | Description for Stop a continuous web job for an app, or a deployment slot. |
| <CopyableCode code="stop_network_trace" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Stop ongoing capturing network packets for the site. |
| <CopyableCode code="stop_network_trace_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Stop ongoing capturing network packets for the site. |
| <CopyableCode code="stop_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Stops an app (or deployment slot, if specified). |
| <CopyableCode code="stop_web_site_network_trace" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Stop ongoing capturing network packets for the site. |
| <CopyableCode code="stop_web_site_network_trace_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Stop ongoing capturing network packets for the site. |
| <CopyableCode code="swap_slot_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, data__preserveVnet, data__targetSlot" /> | Description for Swaps two deployment slots of an app. |
| <CopyableCode code="swap_slot_with_production" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot" /> | Description for Swaps two deployment slots of an app. |
| <CopyableCode code="sync_function_triggers" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Syncs function trigger metadata to the management database |
| <CopyableCode code="sync_function_triggers_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Syncs function trigger metadata to the management database |
| <CopyableCode code="sync_functions" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Syncs function trigger metadata to the management database |
| <CopyableCode code="sync_functions_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Syncs function trigger metadata to the management database |
| <CopyableCode code="sync_repository" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Sync web app repository. |
| <CopyableCode code="sync_repository_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Sync web app repository. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |

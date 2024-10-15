---
title: web_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps
  - app_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>web_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | ProcessModuleInfo resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the details of a web, mobile, or API app. |
| <CopyableCode code="get_diagnostic_logs_config" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the logging configuration of an app. |
| <CopyableCode code="get_diagnostic_logs_config_slot" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the logging configuration of an app. |
| <CopyableCode code="get_instance_function_slot" /> | `SELECT` | <CopyableCode code="functionName, name, resourceGroupName, slot, subscriptionId" /> | Description for Get function information by its ID for web site, or a deployment slot. |
| <CopyableCode code="get_instance_ms_deploy_log" /> | `SELECT` | <CopyableCode code="instanceId, name, resourceGroupName, subscriptionId" /> | Description for Get the MSDeploy Log for the last MSDeploy operation. |
| <CopyableCode code="get_instance_ms_deploy_log_slot" /> | `SELECT` | <CopyableCode code="instanceId, name, resourceGroupName, slot, subscriptionId" /> | Description for Get the MSDeploy Log for the last MSDeploy operation. |
| <CopyableCode code="get_instance_ms_deploy_status" /> | `SELECT` | <CopyableCode code="instanceId, name, resourceGroupName, subscriptionId" /> | Description for Get the status of the last MSDeploy operation. |
| <CopyableCode code="get_instance_ms_deploy_status_slot" /> | `SELECT` | <CopyableCode code="instanceId, name, resourceGroupName, slot, subscriptionId" /> | Description for Get the status of the last MSDeploy operation. |
| <CopyableCode code="get_instance_process" /> | `SELECT` | <CopyableCode code="instanceId, name, processId, resourceGroupName, subscriptionId" /> | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="get_instance_process_module" /> | `SELECT` | <CopyableCode code="baseAddress, instanceId, name, processId, resourceGroupName, subscriptionId" /> | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="get_instance_process_module_slot" /> | `SELECT` | <CopyableCode code="baseAddress, instanceId, name, processId, resourceGroupName, slot, subscriptionId" /> | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="get_instance_process_slot" /> | `SELECT` | <CopyableCode code="instanceId, name, processId, resourceGroupName, slot, subscriptionId" /> | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="get_instance_workflow_slot" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, workflowName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all apps for a subscription. |
| <CopyableCode code="list_backup_slots" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets existing backups of an app. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Gets all web, mobile, and API apps in the specified resource group. |
| <CopyableCode code="list_instance_functions_slot" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for List the functions for a web site, or a deployment slot. |
| <CopyableCode code="list_instance_identifiers" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets all scale-out instances of an app. |
| <CopyableCode code="list_instance_identifiers_slot" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets all scale-out instances of an app. |
| <CopyableCode code="list_instance_process_modules" /> | `SELECT` | <CopyableCode code="instanceId, name, processId, resourceGroupName, subscriptionId" /> | Description for List module information for a process by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="list_instance_process_modules_slot" /> | `SELECT` | <CopyableCode code="instanceId, name, processId, resourceGroupName, slot, subscriptionId" /> | Description for List module information for a process by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="list_instance_process_threads" /> | `SELECT` | <CopyableCode code="instanceId, name, processId, resourceGroupName, subscriptionId" /> | Description for List the threads in a process by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="list_instance_process_threads_slot" /> | `SELECT` | <CopyableCode code="instanceId, name, processId, resourceGroupName, slot, subscriptionId" /> | Description for List the threads in a process by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="list_instance_processes" /> | `SELECT` | <CopyableCode code="instanceId, name, resourceGroupName, subscriptionId" /> | Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. |
| <CopyableCode code="list_instance_processes_slot" /> | `SELECT` | <CopyableCode code="instanceId, name, resourceGroupName, slot, subscriptionId" /> | Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. |
| <CopyableCode code="list_instance_workflows_slot" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Deletes a web, mobile, or API app, or one of the deployment slots. |
| <CopyableCode code="delete_instance_function_slot" /> | `DELETE` | <CopyableCode code="functionName, name, resourceGroupName, slot, subscriptionId" /> | Description for Delete a function for web site, or a deployment slot. |
| <CopyableCode code="delete_instance_process" /> | `DELETE` | <CopyableCode code="instanceId, name, processId, resourceGroupName, subscriptionId" /> | Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. |
| <CopyableCode code="delete_instance_process_slot" /> | `DELETE` | <CopyableCode code="instanceId, name, processId, resourceGroupName, slot, subscriptionId" /> | Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
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
| <CopyableCode code="get_instance_process_dump" /> | `EXEC` | <CopyableCode code="instanceId, name, processId, resourceGroupName, subscriptionId" /> | Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. |
| <CopyableCode code="get_instance_process_dump_slot" /> | `EXEC` | <CopyableCode code="instanceId, name, processId, resourceGroupName, slot, subscriptionId" /> | Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. |
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

## `SELECT` examples

Description for Get all apps for a subscription.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.web_apps
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_apps</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.app_service.web_apps (
name,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties,
identity,
extendedLocation
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ identity }}',
'{{ extendedLocation }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: state
          value: string
        - name: hostNames
          value:
            - string
        - name: repositorySiteName
          value: string
        - name: usageState
          value: string
        - name: enabled
          value: boolean
        - name: enabledHostNames
          value:
            - string
        - name: availabilityState
          value: string
        - name: hostNameSslStates
          value:
            - - name: name
                value: string
              - name: sslState
                value: string
              - name: virtualIP
                value: string
              - name: thumbprint
                value: string
              - name: toUpdate
                value: boolean
              - name: hostType
                value: string
        - name: serverFarmId
          value: string
        - name: reserved
          value: boolean
        - name: isXenon
          value: boolean
        - name: hyperV
          value: boolean
        - name: lastModifiedTimeUtc
          value: string
        - name: dnsConfiguration
          value:
            - name: dnsServers
              value:
                - string
            - name: dnsAltServer
              value: string
            - name: dnsRetryAttemptTimeout
              value: integer
            - name: dnsRetryAttemptCount
              value: integer
            - name: dnsMaxCacheTimeout
              value: integer
            - name: dnsLegacySortOrder
              value: boolean
        - name: vnetRouteAllEnabled
          value: boolean
        - name: vnetImagePullEnabled
          value: boolean
        - name: vnetContentShareEnabled
          value: boolean
        - name: vnetBackupRestoreEnabled
          value: boolean
        - name: siteConfig
          value:
            - name: numberOfWorkers
              value: integer
            - name: defaultDocuments
              value:
                - string
            - name: netFrameworkVersion
              value: string
            - name: phpVersion
              value: string
            - name: pythonVersion
              value: string
            - name: nodeVersion
              value: string
            - name: powerShellVersion
              value: string
            - name: linuxFxVersion
              value: string
            - name: windowsFxVersion
              value: string
            - name: requestTracingEnabled
              value: boolean
            - name: requestTracingExpirationTime
              value: string
            - name: remoteDebuggingEnabled
              value: boolean
            - name: remoteDebuggingVersion
              value: string
            - name: httpLoggingEnabled
              value: boolean
            - name: acrUseManagedIdentityCreds
              value: boolean
            - name: acrUserManagedIdentityID
              value: string
            - name: logsDirectorySizeLimit
              value: integer
            - name: detailedErrorLoggingEnabled
              value: boolean
            - name: publishingUsername
              value: string
            - name: appSettings
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: metadata
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: connectionStrings
              value:
                - - name: name
                    value: string
                  - name: connectionString
                    value: string
                  - name: type
                    value: string
            - name: machineKey
              value:
                - name: validation
                  value: string
                - name: validationKey
                  value: string
                - name: decryption
                  value: string
                - name: decryptionKey
                  value: string
            - name: handlerMappings
              value:
                - - name: extension
                    value: string
                  - name: scriptProcessor
                    value: string
                  - name: arguments
                    value: string
            - name: documentRoot
              value: string
            - name: scmType
              value: string
            - name: use32BitWorkerProcess
              value: boolean
            - name: webSocketsEnabled
              value: boolean
            - name: alwaysOn
              value: boolean
            - name: javaVersion
              value: string
            - name: javaContainer
              value: string
            - name: javaContainerVersion
              value: string
            - name: appCommandLine
              value: string
            - name: managedPipelineMode
              value: string
            - name: virtualApplications
              value:
                - - name: virtualPath
                    value: string
                  - name: physicalPath
                    value: string
                  - name: preloadEnabled
                    value: boolean
                  - name: virtualDirectories
                    value:
                      - - name: virtualPath
                          value: string
                        - name: physicalPath
                          value: string
            - name: loadBalancing
              value: string
            - name: experiments
              value:
                - name: rampUpRules
                  value:
                    - - name: actionHostName
                        value: string
                      - name: reroutePercentage
                        value: number
                      - name: changeStep
                        value: number
                      - name: changeIntervalInMinutes
                        value: integer
                      - name: minReroutePercentage
                        value: number
                      - name: maxReroutePercentage
                        value: number
                      - name: changeDecisionCallbackUrl
                        value: string
                      - name: name
                        value: string
            - name: limits
              value:
                - name: maxPercentageCpu
                  value: number
                - name: maxMemoryInMb
                  value: integer
                - name: maxDiskSizeInMb
                  value: integer
            - name: autoHealEnabled
              value: boolean
            - name: autoHealRules
              value:
                - name: triggers
                  value:
                    - name: requests
                      value:
                        - name: count
                          value: integer
                        - name: timeInterval
                          value: string
                    - name: privateBytesInKB
                      value: integer
                    - name: statusCodes
                      value:
                        - - name: status
                            value: integer
                          - name: subStatus
                            value: integer
                          - name: win32Status
                            value: integer
                          - name: count
                            value: integer
                          - name: timeInterval
                            value: string
                          - name: path
                            value: string
                    - name: slowRequests
                      value:
                        - name: timeTaken
                          value: string
                        - name: path
                          value: string
                        - name: count
                          value: integer
                        - name: timeInterval
                          value: string
                    - name: slowRequestsWithPath
                      value:
                        - - name: timeTaken
                            value: string
                          - name: path
                            value: string
                          - name: count
                            value: integer
                          - name: timeInterval
                            value: string
                    - name: statusCodesRange
                      value:
                        - - name: statusCodes
                            value: string
                          - name: path
                            value: string
                          - name: count
                            value: integer
                          - name: timeInterval
                            value: string
                - name: actions
                  value:
                    - name: actionType
                      value: string
                    - name: customAction
                      value:
                        - name: exe
                          value: string
                        - name: parameters
                          value: string
                    - name: minProcessExecutionTime
                      value: string
            - name: tracingOptions
              value: string
            - name: vnetName
              value: string
            - name: vnetRouteAllEnabled
              value: boolean
            - name: vnetPrivatePortsCount
              value: integer
            - name: cors
              value:
                - name: allowedOrigins
                  value:
                    - string
                - name: supportCredentials
                  value: boolean
            - name: push
              value:
                - name: id
                  value: string
                - name: name
                  value: string
                - name: kind
                  value: string
                - name: type
                  value: string
                - name: properties
                  value:
                    - name: isPushEnabled
                      value: boolean
                    - name: tagWhitelistJson
                      value: string
                    - name: tagsRequiringAuth
                      value: string
                    - name: dynamicTagsJson
                      value: string
            - name: apiDefinition
              value:
                - name: url
                  value: string
            - name: apiManagementConfig
              value:
                - name: id
                  value: string
            - name: autoSwapSlotName
              value: string
            - name: localMySqlEnabled
              value: boolean
            - name: managedServiceIdentityId
              value: integer
            - name: xManagedServiceIdentityId
              value: integer
            - name: keyVaultReferenceIdentity
              value: string
            - name: ipSecurityRestrictions
              value:
                - - name: ipAddress
                    value: string
                  - name: subnetMask
                    value: string
                  - name: vnetSubnetResourceId
                    value: string
                  - name: vnetTrafficTag
                    value: integer
                  - name: subnetTrafficTag
                    value: integer
                  - name: action
                    value: string
                  - name: tag
                    value: string
                  - name: priority
                    value: integer
                  - name: name
                    value: string
                  - name: description
                    value: string
                  - name: headers
                    value: object
            - name: ipSecurityRestrictionsDefaultAction
              value: string
            - name: scmIpSecurityRestrictions
              value:
                - - name: ipAddress
                    value: string
                  - name: subnetMask
                    value: string
                  - name: vnetSubnetResourceId
                    value: string
                  - name: vnetTrafficTag
                    value: integer
                  - name: subnetTrafficTag
                    value: integer
                  - name: action
                    value: string
                  - name: tag
                    value: string
                  - name: priority
                    value: integer
                  - name: name
                    value: string
                  - name: description
                    value: string
                  - name: headers
                    value: object
            - name: scmIpSecurityRestrictionsDefaultAction
              value: string
            - name: scmIpSecurityRestrictionsUseMain
              value: boolean
            - name: http20Enabled
              value: boolean
            - name: minTlsVersion
              value: string
            - name: minTlsCipherSuite
              value: string
            - name: scmMinTlsVersion
              value: string
            - name: ftpsState
              value: string
            - name: preWarmedInstanceCount
              value: integer
            - name: functionAppScaleLimit
              value: integer
            - name: elasticWebAppScaleLimit
              value: integer
            - name: healthCheckPath
              value: string
            - name: functionsRuntimeScaleMonitoringEnabled
              value: boolean
            - name: websiteTimeZone
              value: string
            - name: minimumElasticInstanceCount
              value: integer
            - name: azureStorageAccounts
              value: object
            - name: publicNetworkAccess
              value: string
        - name: functionAppConfig
          value:
            - name: deployment
              value:
                - name: storage
                  value:
                    - name: type
                      value: string
                    - name: value
                      value: string
                    - name: authentication
                      value:
                        - name: type
                          value: string
                        - name: userAssignedIdentityResourceId
                          value: string
                        - name: storageAccountConnectionStringName
                          value: string
            - name: runtime
              value:
                - name: name
                  value: string
                - name: version
                  value: string
            - name: scaleAndConcurrency
              value:
                - name: alwaysReady
                  value:
                    - - name: name
                        value: string
                      - name: instanceCount
                        value: integer
                - name: maximumInstanceCount
                  value: integer
                - name: instanceMemoryMB
                  value: integer
                - name: triggers
                  value:
                    - name: http
                      value:
                        - name: perInstanceConcurrency
                          value: integer
        - name: daprConfig
          value:
            - name: enabled
              value: boolean
            - name: appId
              value: string
            - name: appPort
              value: integer
            - name: httpReadBufferSize
              value: integer
            - name: httpMaxRequestSize
              value: integer
            - name: logLevel
              value: string
            - name: enableApiLogging
              value: boolean
        - name: workloadProfileName
          value: string
        - name: resourceConfig
          value:
            - name: cpu
              value: number
            - name: memory
              value: string
        - name: trafficManagerHostNames
          value:
            - string
        - name: scmSiteAlsoStopped
          value: boolean
        - name: targetSwapSlot
          value: string
        - name: hostingEnvironmentProfile
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: type
              value: string
        - name: clientAffinityEnabled
          value: boolean
        - name: clientCertEnabled
          value: boolean
        - name: clientCertMode
          value: string
        - name: clientCertExclusionPaths
          value: string
        - name: hostNamesDisabled
          value: boolean
        - name: customDomainVerificationId
          value: string
        - name: outboundIpAddresses
          value: string
        - name: possibleOutboundIpAddresses
          value: string
        - name: containerSize
          value: integer
        - name: dailyMemoryTimeQuota
          value: integer
        - name: suspendedTill
          value: string
        - name: maxNumberOfWorkers
          value: integer
        - name: cloningInfo
          value:
            - name: correlationId
              value: string
            - name: overwrite
              value: boolean
            - name: cloneCustomHostNames
              value: boolean
            - name: cloneSourceControl
              value: boolean
            - name: sourceWebAppId
              value: string
            - name: sourceWebAppLocation
              value: string
            - name: hostingEnvironment
              value: string
            - name: appSettingsOverrides
              value: object
            - name: configureLoadBalancing
              value: boolean
            - name: trafficManagerProfileId
              value: string
            - name: trafficManagerProfileName
              value: string
        - name: resourceGroup
          value: string
        - name: isDefaultContainer
          value: boolean
        - name: defaultHostName
          value: string
        - name: slotSwapStatus
          value:
            - name: timestampUtc
              value: string
            - name: sourceSlotName
              value: string
            - name: destinationSlotName
              value: string
        - name: httpsOnly
          value: boolean
        - name: redundancyMode
          value: string
        - name: inProgressOperationId
          value: string
        - name: publicNetworkAccess
          value: string
        - name: storageAccountRequired
          value: boolean
        - name: keyVaultReferenceIdentity
          value: string
        - name: virtualNetworkSubnetId
          value: string
        - name: managedEnvironmentId
          value: string
    - name: identity
      value:
        - name: type
          value: string
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: userAssignedIdentities
          value: object
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>web_apps</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.web_apps
SET 
kind = '{{ kind }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>web_apps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.web_apps
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

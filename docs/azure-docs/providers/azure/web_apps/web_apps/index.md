---
title: web_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps
  - web_apps
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
<tr><td><b>Id</b></td><td><code>azure.web_apps.web_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `identity` | `object` | Managed service identity. |
| `properties` | `object` | Site resource specific properties |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `extendedLocation` | `object` | Extended Location. |
| `location` | `string` | Resource Location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebApps_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Description for Gets the details of a web, mobile, or API app. |
| `WebApps_List` | `SELECT` | `subscriptionId` | Description for Get all apps for a subscription. |
| `WebApps_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Gets all web, mobile, and API apps in the specified resource group. |
| `WebApps_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId` | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| `WebApps_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Description for Deletes a web, mobile, or API app, or one of the deployment slots. |
| `WebApps_AddPremierAddOn` | `EXEC` | `name, premierAddOnName, resourceGroupName, subscriptionId` | Description for Updates a named add-on of an app. |
| `WebApps_AddPremierAddOnSlot` | `EXEC` | `name, premierAddOnName, resourceGroupName, slot, subscriptionId` | Description for Updates a named add-on of an app. |
| `WebApps_AnalyzeCustomHostname` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Analyze a custom hostname. |
| `WebApps_AnalyzeCustomHostnameSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Analyze a custom hostname. |
| `WebApps_ApplySlotConfigToProduction` | `EXEC` | `name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Applies the configuration settings from the target slot onto the current slot. |
| `WebApps_ApplySlotConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Applies the configuration settings from the target slot onto the current slot. |
| `WebApps_ApproveOrRejectPrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `WebApps_ApproveOrRejectPrivateEndpointConnectionSlot` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, slot, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `WebApps_Backup` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates a backup of an app. |
| `WebApps_BackupSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Creates a backup of an app. |
| `WebApps_CreateDeployment` | `EXEC` | `id, name, resourceGroupName, subscriptionId` | Description for Create a deployment for an app, or a deployment slot. |
| `WebApps_CreateDeploymentSlot` | `EXEC` | `id, name, resourceGroupName, slot, subscriptionId` | Description for Create a deployment for an app, or a deployment slot. |
| `WebApps_CreateFunction` | `EXEC` | `functionName, name, resourceGroupName, subscriptionId` | Description for Create function for web site, or a deployment slot. |
| `WebApps_CreateInstanceFunctionSlot` | `EXEC` | `functionName, name, resourceGroupName, slot, subscriptionId` | Description for Create function for web site, or a deployment slot. |
| `WebApps_CreateInstanceMSDeployOperation` | `EXEC` | `instanceId, name, resourceGroupName, subscriptionId` | Description for Invoke the MSDeploy web app extension. |
| `WebApps_CreateInstanceMSDeployOperationSlot` | `EXEC` | `instanceId, name, resourceGroupName, slot, subscriptionId` | Description for Invoke the MSDeploy web app extension. |
| `WebApps_CreateMSDeployOperation` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Invoke the MSDeploy web app extension. |
| `WebApps_CreateMSDeployOperationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Invoke the MSDeploy web app extension. |
| `WebApps_CreateOneDeployOperation` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Invoke the OneDeploy publish web app extension. |
| `WebApps_CreateOrUpdateConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the configuration of an app. |
| `WebApps_CreateOrUpdateConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the configuration of an app. |
| `WebApps_CreateOrUpdateDomainOwnershipIdentifier` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId` | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |
| `WebApps_CreateOrUpdateDomainOwnershipIdentifierSlot` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |
| `WebApps_CreateOrUpdateFunctionSecret` | `EXEC` | `functionName, keyName, name, resourceGroupName, subscriptionId` | Description for Add or update a function secret. |
| `WebApps_CreateOrUpdateFunctionSecretSlot` | `EXEC` | `functionName, keyName, name, resourceGroupName, slot, subscriptionId` | Description for Add or update a function secret. |
| `WebApps_CreateOrUpdateHostNameBinding` | `EXEC` | `hostName, name, resourceGroupName, subscriptionId` | Description for Creates a hostname binding for an app. |
| `WebApps_CreateOrUpdateHostNameBindingSlot` | `EXEC` | `hostName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a hostname binding for an app. |
| `WebApps_CreateOrUpdateHostSecret` | `EXEC` | `keyName, keyType, name, resourceGroupName, subscriptionId` | Description for Add or update a host level secret. |
| `WebApps_CreateOrUpdateHostSecretSlot` | `EXEC` | `keyName, keyType, name, resourceGroupName, slot, subscriptionId` | Description for Add or update a host level secret. |
| `WebApps_CreateOrUpdateHybridConnection` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Creates a new Hybrid Connection using a Service Bus relay. |
| `WebApps_CreateOrUpdateHybridConnectionSlot` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, slot, subscriptionId` | Description for Creates a new Hybrid Connection using a Service Bus relay. |
| `WebApps_CreateOrUpdatePublicCertificate` | `EXEC` | `name, publicCertificateName, resourceGroupName, subscriptionId` | Description for Creates a hostname binding for an app. |
| `WebApps_CreateOrUpdatePublicCertificateSlot` | `EXEC` | `name, publicCertificateName, resourceGroupName, slot, subscriptionId` | Description for Creates a hostname binding for an app. |
| `WebApps_CreateOrUpdateRelayServiceConnection` | `EXEC` | `entityName, name, resourceGroupName, subscriptionId` | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |
| `WebApps_CreateOrUpdateRelayServiceConnectionSlot` | `EXEC` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |
| `WebApps_CreateOrUpdateSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| `WebApps_CreateOrUpdateSourceControl` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the source control configuration of an app. |
| `WebApps_CreateOrUpdateSourceControlSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the source control configuration of an app. |
| `WebApps_CreateOrUpdateSwiftVirtualNetworkConnectionWithCheck` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not<br />in use by another App Service Plan other than the one this App is in. |
| `WebApps_CreateOrUpdateSwiftVirtualNetworkConnectionWithCheckSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not<br />in use by another App Service Plan other than the one this App is in. |
| `WebApps_CreateOrUpdateVnetConnection` | `EXEC` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
| `WebApps_CreateOrUpdateVnetConnectionGateway` | `EXEC` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
| `WebApps_CreateOrUpdateVnetConnectionGatewaySlot` | `EXEC` | `gatewayName, name, resourceGroupName, slot, subscriptionId, vnetName` | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
| `WebApps_CreateOrUpdateVnetConnectionSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, vnetName` | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
| `WebApps_DeleteBackup` | `EXEC` | `backupId, name, resourceGroupName, subscriptionId` | Description for Deletes a backup of an app by its ID. |
| `WebApps_DeleteBackupConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Deletes the backup configuration of an app. |
| `WebApps_DeleteBackupConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Deletes the backup configuration of an app. |
| `WebApps_DeleteBackupSlot` | `EXEC` | `backupId, name, resourceGroupName, slot, subscriptionId` | Description for Deletes a backup of an app by its ID. |
| `WebApps_DeleteContinuousWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Delete a continuous web job by its ID for an app, or a deployment slot. |
| `WebApps_DeleteContinuousWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Delete a continuous web job by its ID for an app, or a deployment slot. |
| `WebApps_DeleteDeployment` | `EXEC` | `id, name, resourceGroupName, subscriptionId` | Description for Delete a deployment by its ID for an app, or a deployment slot. |
| `WebApps_DeleteDeploymentSlot` | `EXEC` | `id, name, resourceGroupName, slot, subscriptionId` | Description for Delete a deployment by its ID for an app, or a deployment slot. |
| `WebApps_DeleteDomainOwnershipIdentifier` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId` | Description for Deletes a domain ownership identifier for a web app. |
| `WebApps_DeleteDomainOwnershipIdentifierSlot` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Deletes a domain ownership identifier for a web app. |
| `WebApps_DeleteFunction` | `EXEC` | `functionName, name, resourceGroupName, subscriptionId` | Description for Delete a function for web site, or a deployment slot. |
| `WebApps_DeleteFunctionSecret` | `EXEC` | `functionName, keyName, name, resourceGroupName, subscriptionId` | Description for Delete a function secret. |
| `WebApps_DeleteFunctionSecretSlot` | `EXEC` | `functionName, keyName, name, resourceGroupName, slot, subscriptionId` | Description for Delete a function secret. |
| `WebApps_DeleteHostNameBinding` | `EXEC` | `hostName, name, resourceGroupName, subscriptionId` | Description for Deletes a hostname binding for an app. |
| `WebApps_DeleteHostNameBindingSlot` | `EXEC` | `hostName, name, resourceGroupName, slot, subscriptionId` | Description for Deletes a hostname binding for an app. |
| `WebApps_DeleteHostSecret` | `EXEC` | `keyName, keyType, name, resourceGroupName, subscriptionId` | Description for Delete a host level secret. |
| `WebApps_DeleteHostSecretSlot` | `EXEC` | `keyName, keyType, name, resourceGroupName, slot, subscriptionId` | Description for Delete a host level secret. |
| `WebApps_DeleteHybridConnection` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Removes a Hybrid Connection from this site. |
| `WebApps_DeleteHybridConnectionSlot` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, slot, subscriptionId` | Description for Removes a Hybrid Connection from this site. |
| `WebApps_DeleteInstanceFunctionSlot` | `EXEC` | `functionName, name, resourceGroupName, slot, subscriptionId` | Description for Delete a function for web site, or a deployment slot. |
| `WebApps_DeleteInstanceProcess` | `EXEC` | `instanceId, name, processId, resourceGroupName, subscriptionId` | Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. |
| `WebApps_DeleteInstanceProcessSlot` | `EXEC` | `instanceId, name, processId, resourceGroupName, slot, subscriptionId` | Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. |
| `WebApps_DeletePremierAddOn` | `EXEC` | `name, premierAddOnName, resourceGroupName, subscriptionId` | Description for Delete a premier add-on from an app. |
| `WebApps_DeletePremierAddOnSlot` | `EXEC` | `name, premierAddOnName, resourceGroupName, slot, subscriptionId` | Description for Delete a premier add-on from an app. |
| `WebApps_DeletePrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Deletes a private endpoint connection |
| `WebApps_DeletePrivateEndpointConnectionSlot` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, slot, subscriptionId` | Description for Deletes a private endpoint connection |
| `WebApps_DeleteProcess` | `EXEC` | `name, processId, resourceGroupName, subscriptionId` | Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. |
| `WebApps_DeleteProcessSlot` | `EXEC` | `name, processId, resourceGroupName, slot, subscriptionId` | Description for Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site. |
| `WebApps_DeletePublicCertificate` | `EXEC` | `name, publicCertificateName, resourceGroupName, subscriptionId` | Description for Deletes a hostname binding for an app. |
| `WebApps_DeletePublicCertificateSlot` | `EXEC` | `name, publicCertificateName, resourceGroupName, slot, subscriptionId` | Description for Deletes a hostname binding for an app. |
| `WebApps_DeleteRelayServiceConnection` | `EXEC` | `entityName, name, resourceGroupName, subscriptionId` | Description for Deletes a relay service connection by its name. |
| `WebApps_DeleteRelayServiceConnectionSlot` | `EXEC` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Deletes a relay service connection by its name. |
| `WebApps_DeleteSiteExtension` | `EXEC` | `name, resourceGroupName, siteExtensionId, subscriptionId` | Description for Remove a site extension from a web site, or a deployment slot. |
| `WebApps_DeleteSiteExtensionSlot` | `EXEC` | `name, resourceGroupName, siteExtensionId, slot, subscriptionId` | Description for Remove a site extension from a web site, or a deployment slot. |
| `WebApps_DeleteSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Deletes a web, mobile, or API app, or one of the deployment slots. |
| `WebApps_DeleteSourceControl` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Deletes the source control configuration of an app. |
| `WebApps_DeleteSourceControlSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Deletes the source control configuration of an app. |
| `WebApps_DeleteSwiftVirtualNetwork` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Deletes a Swift Virtual Network connection from an app (or deployment slot). |
| `WebApps_DeleteSwiftVirtualNetworkSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Deletes a Swift Virtual Network connection from an app (or deployment slot). |
| `WebApps_DeleteTriggeredWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Delete a triggered web job by its ID for an app, or a deployment slot. |
| `WebApps_DeleteTriggeredWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Delete a triggered web job by its ID for an app, or a deployment slot. |
| `WebApps_DeleteVnetConnection` | `EXEC` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Deletes a connection from an app (or deployment slot to a named virtual network. |
| `WebApps_DeleteVnetConnectionSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, vnetName` | Description for Deletes a connection from an app (or deployment slot to a named virtual network. |
| `WebApps_DiscoverBackup` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. |
| `WebApps_DiscoverBackupSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Discovers an existing app backup that can be restored from a blob in Azure storage. Use this to get information about the databases stored in a backup. |
| `WebApps_GenerateNewSitePublishingPassword` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Generates a new publishing password for an app (or deployment slot, if specified). |
| `WebApps_GenerateNewSitePublishingPasswordSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Generates a new publishing password for an app (or deployment slot, if specified). |
| `WebApps_GetAppSettingKeyVaultReference` | `EXEC` | `appSettingKey, name, resourceGroupName, subscriptionId` | Description for Gets the config reference and status of an app |
| `WebApps_GetAppSettingKeyVaultReferenceSlot` | `EXEC` | `appSettingKey, name, resourceGroupName, slot, subscriptionId` | Description for Gets the config reference and status of an app |
| `WebApps_GetAppSettingsKeyVaultReferences` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the config reference app settings and status of an app |
| `WebApps_GetAppSettingsKeyVaultReferencesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the config reference app settings and status of an app |
| `WebApps_GetAuthSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the Authentication/Authorization settings of an app. |
| `WebApps_GetAuthSettingsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the Authentication/Authorization settings of an app. |
| `WebApps_GetAuthSettingsV2` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets site's Authentication / Authorization settings for apps via the V2 format |
| `WebApps_GetAuthSettingsV2Slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets site's Authentication / Authorization settings for apps via the V2 format |
| `WebApps_GetAuthSettingsV2WithoutSecrets` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets site's Authentication / Authorization settings for apps via the V2 format |
| `WebApps_GetAuthSettingsV2WithoutSecretsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` |  |
| `WebApps_GetBackupConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the backup configuration of an app. |
| `WebApps_GetBackupConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the backup configuration of an app. |
| `WebApps_GetBackupStatus` | `EXEC` | `backupId, name, resourceGroupName, subscriptionId` | Description for Gets a backup of an app by its ID. |
| `WebApps_GetBackupStatusSlot` | `EXEC` | `backupId, name, resourceGroupName, slot, subscriptionId` | Description for Gets a backup of an app by its ID. |
| `WebApps_GetConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc. |
| `WebApps_GetConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc. |
| `WebApps_GetConfigurationSnapshot` | `EXEC` | `name, resourceGroupName, snapshotId, subscriptionId` | Description for Gets a snapshot of the configuration of an app at a previous point in time. |
| `WebApps_GetConfigurationSnapshotSlot` | `EXEC` | `name, resourceGroupName, slot, snapshotId, subscriptionId` | Description for Gets a snapshot of the configuration of an app at a previous point in time. |
| `WebApps_GetContainerLogsZip` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the ZIP archived docker log files for the given site |
| `WebApps_GetContainerLogsZipSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the ZIP archived docker log files for the given site |
| `WebApps_GetContinuousWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Gets a continuous web job by its ID for an app, or a deployment slot. |
| `WebApps_GetContinuousWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Gets a continuous web job by its ID for an app, or a deployment slot. |
| `WebApps_GetDeployment` | `EXEC` | `id, name, resourceGroupName, subscriptionId` | Description for Get a deployment by its ID for an app, or a deployment slot. |
| `WebApps_GetDeploymentSlot` | `EXEC` | `id, name, resourceGroupName, slot, subscriptionId` | Description for Get a deployment by its ID for an app, or a deployment slot. |
| `WebApps_GetDiagnosticLogsConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the logging configuration of an app. |
| `WebApps_GetDiagnosticLogsConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the logging configuration of an app. |
| `WebApps_GetDomainOwnershipIdentifier` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId` | Description for Get domain ownership identifier for web app. |
| `WebApps_GetDomainOwnershipIdentifierSlot` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Get domain ownership identifier for web app. |
| `WebApps_GetFtpAllowed` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Returns whether FTP is allowed on the site or not. |
| `WebApps_GetFtpAllowedSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Returns whether FTP is allowed on the site or not. |
| `WebApps_GetFunction` | `EXEC` | `functionName, name, resourceGroupName, subscriptionId` | Description for Get function information by its ID for web site, or a deployment slot. |
| `WebApps_GetFunctionsAdminToken` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Fetch a short lived token that can be exchanged for a master key. |
| `WebApps_GetFunctionsAdminTokenSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Fetch a short lived token that can be exchanged for a master key. |
| `WebApps_GetHostNameBinding` | `EXEC` | `hostName, name, resourceGroupName, subscriptionId` | Description for Get the named hostname binding for an app (or deployment slot, if specified). |
| `WebApps_GetHostNameBindingSlot` | `EXEC` | `hostName, name, resourceGroupName, slot, subscriptionId` | Description for Get the named hostname binding for an app (or deployment slot, if specified). |
| `WebApps_GetHybridConnection` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App. |
| `WebApps_GetHybridConnectionSlot` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, slot, subscriptionId` | Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App. |
| `WebApps_GetInstanceFunctionSlot` | `EXEC` | `functionName, name, resourceGroupName, slot, subscriptionId` | Description for Get function information by its ID for web site, or a deployment slot. |
| `WebApps_GetInstanceInfo` | `EXEC` | `instanceId, name, resourceGroupName, subscriptionId` | Description for Gets all scale-out instances of an app. |
| `WebApps_GetInstanceInfoSlot` | `EXEC` | `instanceId, name, resourceGroupName, slot, subscriptionId` | Description for Gets all scale-out instances of an app. |
| `WebApps_GetInstanceMSDeployLog` | `EXEC` | `instanceId, name, resourceGroupName, subscriptionId` | Description for Get the MSDeploy Log for the last MSDeploy operation. |
| `WebApps_GetInstanceMSDeployLogSlot` | `EXEC` | `instanceId, name, resourceGroupName, slot, subscriptionId` | Description for Get the MSDeploy Log for the last MSDeploy operation. |
| `WebApps_GetInstanceMsDeployStatus` | `EXEC` | `instanceId, name, resourceGroupName, subscriptionId` | Description for Get the status of the last MSDeploy operation. |
| `WebApps_GetInstanceMsDeployStatusSlot` | `EXEC` | `instanceId, name, resourceGroupName, slot, subscriptionId` | Description for Get the status of the last MSDeploy operation. |
| `WebApps_GetInstanceProcess` | `EXEC` | `instanceId, name, processId, resourceGroupName, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetInstanceProcessDump` | `EXEC` | `instanceId, name, processId, resourceGroupName, subscriptionId` | Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetInstanceProcessDumpSlot` | `EXEC` | `instanceId, name, processId, resourceGroupName, slot, subscriptionId` | Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetInstanceProcessModule` | `EXEC` | `baseAddress, instanceId, name, processId, resourceGroupName, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetInstanceProcessModuleSlot` | `EXEC` | `baseAddress, instanceId, name, processId, resourceGroupName, slot, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetInstanceProcessSlot` | `EXEC` | `instanceId, name, processId, resourceGroupName, slot, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetMSDeployLog` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get the MSDeploy Log for the last MSDeploy operation. |
| `WebApps_GetMSDeployLogSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Get the MSDeploy Log for the last MSDeploy operation. |
| `WebApps_GetMSDeployStatus` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get the status of the last MSDeploy operation. |
| `WebApps_GetMSDeployStatusSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Get the status of the last MSDeploy operation. |
| `WebApps_GetMigrateMySqlStatus` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled |
| `WebApps_GetMigrateMySqlStatusSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled |
| `WebApps_GetNetworkTraceOperation` | `EXEC` | `name, operationId, resourceGroupName, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetNetworkTraceOperationSlot` | `EXEC` | `name, operationId, resourceGroupName, slot, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetNetworkTraceOperationSlotV2` | `EXEC` | `name, operationId, resourceGroupName, slot, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetNetworkTraceOperationV2` | `EXEC` | `name, operationId, resourceGroupName, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetNetworkTraces` | `EXEC` | `name, operationId, resourceGroupName, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetNetworkTracesSlot` | `EXEC` | `name, operationId, resourceGroupName, slot, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetNetworkTracesSlotV2` | `EXEC` | `name, operationId, resourceGroupName, slot, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetNetworkTracesV2` | `EXEC` | `name, operationId, resourceGroupName, subscriptionId` | Description for Gets a named operation for a network trace capturing (or deployment slot, if specified). |
| `WebApps_GetOneDeployStatus` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Invoke onedeploy status API /api/deployments and gets the deployment status for the site |
| `WebApps_GetPremierAddOn` | `EXEC` | `name, premierAddOnName, resourceGroupName, subscriptionId` | Description for Gets a named add-on of an app. |
| `WebApps_GetPremierAddOnSlot` | `EXEC` | `name, premierAddOnName, resourceGroupName, slot, subscriptionId` | Description for Gets a named add-on of an app. |
| `WebApps_GetPrivateAccess` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets data around private site access enablement and authorized Virtual Networks that can access the site. |
| `WebApps_GetPrivateAccessSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets data around private site access enablement and authorized Virtual Networks that can access the site. |
| `WebApps_GetPrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Gets a private endpoint connection |
| `WebApps_GetPrivateEndpointConnectionList` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the list of private endpoint connections associated with a site |
| `WebApps_GetPrivateEndpointConnectionListSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the list of private endpoint connections associated with a site |
| `WebApps_GetPrivateEndpointConnectionSlot` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, slot, subscriptionId` | Description for Gets a private endpoint connection |
| `WebApps_GetPrivateLinkResources` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the private link resources |
| `WebApps_GetPrivateLinkResourcesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the private link resources |
| `WebApps_GetProcess` | `EXEC` | `name, processId, resourceGroupName, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetProcessDump` | `EXEC` | `name, processId, resourceGroupName, subscriptionId` | Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetProcessDumpSlot` | `EXEC` | `name, processId, resourceGroupName, slot, subscriptionId` | Description for Get a memory dump of a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetProcessModule` | `EXEC` | `baseAddress, name, processId, resourceGroupName, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetProcessModuleSlot` | `EXEC` | `baseAddress, name, processId, resourceGroupName, slot, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetProcessSlot` | `EXEC` | `name, processId, resourceGroupName, slot, subscriptionId` | Description for Get process information by its ID for a specific scaled-out instance in a web site. |
| `WebApps_GetProductionSiteDeploymentStatus` | `EXEC` | `deploymentStatusId, name, resourceGroupName, subscriptionId` |  |
| `WebApps_GetPublicCertificate` | `EXEC` | `name, publicCertificateName, resourceGroupName, subscriptionId` | Description for Get the named public certificate for an app (or deployment slot, if specified). |
| `WebApps_GetPublicCertificateSlot` | `EXEC` | `name, publicCertificateName, resourceGroupName, slot, subscriptionId` | Description for Get the named public certificate for an app (or deployment slot, if specified). |
| `WebApps_GetRelayServiceConnection` | `EXEC` | `entityName, name, resourceGroupName, subscriptionId` | Description for Gets a hybrid connection configuration by its name. |
| `WebApps_GetRelayServiceConnectionSlot` | `EXEC` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Gets a hybrid connection configuration by its name. |
| `WebApps_GetScmAllowed` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Returns whether Scm basic auth is allowed on the site or not. |
| `WebApps_GetScmAllowedSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Returns whether Scm basic auth is allowed on the site or not. |
| `WebApps_GetSiteConnectionStringKeyVaultReference` | `EXEC` | `connectionStringKey, name, resourceGroupName, subscriptionId` | Description for Gets the config reference and status of an app |
| `WebApps_GetSiteConnectionStringKeyVaultReferenceSlot` | `EXEC` | `connectionStringKey, name, resourceGroupName, slot, subscriptionId` | Description for Gets the config reference and status of an app |
| `WebApps_GetSiteConnectionStringKeyVaultReferences` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the config reference app settings and status of an app |
| `WebApps_GetSiteConnectionStringKeyVaultReferencesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the config reference app settings and status of an app |
| `WebApps_GetSiteExtension` | `EXEC` | `name, resourceGroupName, siteExtensionId, subscriptionId` | Description for Get site extension information by its ID for a web site, or a deployment slot. |
| `WebApps_GetSiteExtensionSlot` | `EXEC` | `name, resourceGroupName, siteExtensionId, slot, subscriptionId` | Description for Get site extension information by its ID for a web site, or a deployment slot. |
| `WebApps_GetSitePhpErrorLogFlag` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets web app's event logs. |
| `WebApps_GetSitePhpErrorLogFlagSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets web app's event logs. |
| `WebApps_GetSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the details of a web, mobile, or API app. |
| `WebApps_GetSlotSiteDeploymentStatusSlot` | `EXEC` | `deploymentStatusId, name, resourceGroupName, slot, subscriptionId` |  |
| `WebApps_GetSourceControl` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the source control configuration of an app. |
| `WebApps_GetSourceControlSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the source control configuration of an app. |
| `WebApps_GetSwiftVirtualNetworkConnection` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets a Swift Virtual Network connection. |
| `WebApps_GetSwiftVirtualNetworkConnectionSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets a Swift Virtual Network connection. |
| `WebApps_GetTriggeredWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Gets a triggered web job by its ID for an app, or a deployment slot. |
| `WebApps_GetTriggeredWebJobHistory` | `EXEC` | `id, name, resourceGroupName, subscriptionId, webJobName` | Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot. |
| `WebApps_GetTriggeredWebJobHistorySlot` | `EXEC` | `id, name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot. |
| `WebApps_GetTriggeredWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Gets a triggered web job by its ID for an app, or a deployment slot. |
| `WebApps_GetVnetConnection` | `EXEC` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Gets a virtual network the app (or deployment slot) is connected to by name. |
| `WebApps_GetVnetConnectionGateway` | `EXEC` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Gets an app's Virtual Network gateway. |
| `WebApps_GetVnetConnectionGatewaySlot` | `EXEC` | `gatewayName, name, resourceGroupName, slot, subscriptionId, vnetName` | Description for Gets an app's Virtual Network gateway. |
| `WebApps_GetVnetConnectionSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, vnetName` | Description for Gets a virtual network the app (or deployment slot) is connected to by name. |
| `WebApps_GetWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Get webjob information for an app, or a deployment slot. |
| `WebApps_GetWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Get webjob information for an app, or a deployment slot. |
| `WebApps_GetWebSiteContainerLogs` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the last lines of docker logs for the given site |
| `WebApps_GetWebSiteContainerLogsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the last lines of docker logs for the given site |
| `WebApps_InstallSiteExtension` | `EXEC` | `name, resourceGroupName, siteExtensionId, subscriptionId` | Description for Install site extension on a web site, or a deployment slot. |
| `WebApps_InstallSiteExtensionSlot` | `EXEC` | `name, resourceGroupName, siteExtensionId, slot, subscriptionId` | Description for Install site extension on a web site, or a deployment slot. |
| `WebApps_IsCloneable` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Shows whether an app can be cloned to another resource group or subscription. |
| `WebApps_IsCloneableSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Shows whether an app can be cloned to another resource group or subscription. |
| `WebApps_ListApplicationSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the application settings of an app. |
| `WebApps_ListApplicationSettingsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the application settings of an app. |
| `WebApps_ListAzureStorageAccounts` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the Azure storage account configurations of an app. |
| `WebApps_ListAzureStorageAccountsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the Azure storage account configurations of an app. |
| `WebApps_ListBackupStatusSecrets` | `EXEC` | `backupId, name, resourceGroupName, subscriptionId` | Description for Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. |
| `WebApps_ListBackupStatusSecretsSlot` | `EXEC` | `backupId, name, resourceGroupName, slot, subscriptionId` | Description for Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body. |
| `WebApps_ListBackups` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets existing backups of an app. |
| `WebApps_ListBackupsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets existing backups of an app. |
| `WebApps_ListBasicPublishingCredentialsPolicies` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site. |
| `WebApps_ListBasicPublishingCredentialsPoliciesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Returns whether Scm basic auth is allowed and whether Ftp is allowed for a given site. |
| `WebApps_ListConfigurationSnapshotInfo` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot. |
| `WebApps_ListConfigurationSnapshotInfoSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot. |
| `WebApps_ListConfigurations` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List the configurations of an app |
| `WebApps_ListConfigurationsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for List the configurations of an app |
| `WebApps_ListConnectionStrings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the connection strings of an app. |
| `WebApps_ListConnectionStringsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the connection strings of an app. |
| `WebApps_ListContinuousWebJobs` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List continuous web jobs for an app, or a deployment slot. |
| `WebApps_ListContinuousWebJobsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for List continuous web jobs for an app, or a deployment slot. |
| `WebApps_ListDeploymentLog` | `EXEC` | `id, name, resourceGroupName, subscriptionId` | Description for List deployment log for specific deployment for an app, or a deployment slot. |
| `WebApps_ListDeploymentLogSlot` | `EXEC` | `id, name, resourceGroupName, slot, subscriptionId` | Description for List deployment log for specific deployment for an app, or a deployment slot. |
| `WebApps_ListDeployments` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List deployments for an app, or a deployment slot. |
| `WebApps_ListDeploymentsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for List deployments for an app, or a deployment slot. |
| `WebApps_ListDomainOwnershipIdentifiers` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Lists ownership identifiers for domain associated with web app. |
| `WebApps_ListDomainOwnershipIdentifiersSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Lists ownership identifiers for domain associated with web app. |
| `WebApps_ListFunctionKeys` | `EXEC` | `functionName, name, resourceGroupName, subscriptionId` | Description for Get function keys for a function in a web site, or a deployment slot. |
| `WebApps_ListFunctionKeysSlot` | `EXEC` | `functionName, name, resourceGroupName, slot, subscriptionId` | Description for Get function keys for a function in a web site, or a deployment slot. |
| `WebApps_ListFunctionSecrets` | `EXEC` | `functionName, name, resourceGroupName, subscriptionId` | Description for Get function secrets for a function in a web site, or a deployment slot. |
| `WebApps_ListFunctionSecretsSlot` | `EXEC` | `functionName, name, resourceGroupName, slot, subscriptionId` | Description for Get function secrets for a function in a web site, or a deployment slot. |
| `WebApps_ListFunctions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List the functions for a web site, or a deployment slot. |
| `WebApps_ListHostKeys` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get host secrets for a function app. |
| `WebApps_ListHostKeysSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Get host secrets for a function app. |
| `WebApps_ListHostNameBindings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get hostname bindings for an app or a deployment slot. |
| `WebApps_ListHostNameBindingsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Get hostname bindings for an app or a deployment slot. |
| `WebApps_ListHybridConnections` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Retrieves all Service Bus Hybrid Connections used by this Web App. |
| `WebApps_ListHybridConnectionsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Retrieves all Service Bus Hybrid Connections used by this Web App. |
| `WebApps_ListInstanceFunctionsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for List the functions for a web site, or a deployment slot. |
| `WebApps_ListInstanceIdentifiers` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets all scale-out instances of an app. |
| `WebApps_ListInstanceIdentifiersSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets all scale-out instances of an app. |
| `WebApps_ListInstanceProcessModules` | `EXEC` | `instanceId, name, processId, resourceGroupName, subscriptionId` | Description for List module information for a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListInstanceProcessModulesSlot` | `EXEC` | `instanceId, name, processId, resourceGroupName, slot, subscriptionId` | Description for List module information for a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListInstanceProcessThreads` | `EXEC` | `instanceId, name, processId, resourceGroupName, subscriptionId` | Description for List the threads in a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListInstanceProcessThreadsSlot` | `EXEC` | `instanceId, name, processId, resourceGroupName, slot, subscriptionId` | Description for List the threads in a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListInstanceProcesses` | `EXEC` | `instanceId, name, resourceGroupName, subscriptionId` | Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. |
| `WebApps_ListInstanceProcessesSlot` | `EXEC` | `instanceId, name, resourceGroupName, slot, subscriptionId` | Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. |
| `WebApps_ListMetadata` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the metadata of an app. |
| `WebApps_ListMetadataSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the metadata of an app. |
| `WebApps_ListNetworkFeatures` | `EXEC` | `name, resourceGroupName, subscriptionId, view` | Description for Gets all network features used by the app (or deployment slot, if specified). |
| `WebApps_ListNetworkFeaturesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, view` | Description for Gets all network features used by the app (or deployment slot, if specified). |
| `WebApps_ListPerfMonCounters` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets perfmon counters for web app. |
| `WebApps_ListPerfMonCountersSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets perfmon counters for web app. |
| `WebApps_ListPremierAddOns` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the premier add-ons of an app. |
| `WebApps_ListPremierAddOnsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the premier add-ons of an app. |
| `WebApps_ListProcessModules` | `EXEC` | `name, processId, resourceGroupName, subscriptionId` | Description for List module information for a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListProcessModulesSlot` | `EXEC` | `name, processId, resourceGroupName, slot, subscriptionId` | Description for List module information for a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListProcessThreads` | `EXEC` | `name, processId, resourceGroupName, subscriptionId` | Description for List the threads in a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListProcessThreadsSlot` | `EXEC` | `name, processId, resourceGroupName, slot, subscriptionId` | Description for List the threads in a process by its ID for a specific scaled-out instance in a web site. |
| `WebApps_ListProcesses` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. |
| `WebApps_ListProcessesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site. |
| `WebApps_ListProductionSiteDeploymentStatuses` | `EXEC` | `name, resourceGroupName, subscriptionId` |  |
| `WebApps_ListPublicCertificates` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get public certificates for an app or a deployment slot. |
| `WebApps_ListPublicCertificatesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Get public certificates for an app or a deployment slot. |
| `WebApps_ListPublishingCredentials` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the Git/FTP publishing credentials of an app. |
| `WebApps_ListPublishingCredentialsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the Git/FTP publishing credentials of an app. |
| `WebApps_ListPublishingProfileXmlWithSecrets` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the publishing profile for an app (or deployment slot, if specified). |
| `WebApps_ListPublishingProfileXmlWithSecretsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the publishing profile for an app (or deployment slot, if specified). |
| `WebApps_ListRelayServiceConnections` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets hybrid connections configured for an app (or deployment slot, if specified). |
| `WebApps_ListRelayServiceConnectionsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets hybrid connections configured for an app (or deployment slot, if specified). |
| `WebApps_ListSiteBackups` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets existing backups of an app. |
| `WebApps_ListSiteBackupsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets existing backups of an app. |
| `WebApps_ListSiteExtensions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Get list of siteextensions for a web site, or a deployment slot. |
| `WebApps_ListSiteExtensionsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Get list of siteextensions for a web site, or a deployment slot. |
| `WebApps_ListSitePushSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the Push settings associated with web app. |
| `WebApps_ListSitePushSettingsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the Push settings associated with web app. |
| `WebApps_ListSlotConfigurationNames` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the names of app settings and connection strings that stick to the slot (not swapped). |
| `WebApps_ListSlotDifferencesFromProduction` | `EXEC` | `name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Get the difference in configuration settings between two web app slots. |
| `WebApps_ListSlotDifferencesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Get the difference in configuration settings between two web app slots. |
| `WebApps_ListSlotSiteDeploymentStatusesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` |  |
| `WebApps_ListSlots` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets an app's deployment slots. |
| `WebApps_ListSnapshots` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Returns all Snapshots to the user. |
| `WebApps_ListSnapshotsFromDRSecondary` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Returns all Snapshots to the user from DRSecondary endpoint. |
| `WebApps_ListSnapshotsFromDRSecondarySlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Returns all Snapshots to the user from DRSecondary endpoint. |
| `WebApps_ListSnapshotsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Returns all Snapshots to the user. |
| `WebApps_ListSyncFunctionTriggers` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for This is to allow calling via powershell and ARM template. |
| `WebApps_ListSyncFunctionTriggersSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for This is to allow calling via powershell and ARM template. |
| `WebApps_ListSyncStatus` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for This is to allow calling via powershell and ARM template. |
| `WebApps_ListSyncStatusSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for This is to allow calling via powershell and ARM template. |
| `WebApps_ListTriggeredWebJobHistory` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for List a triggered web job's history for an app, or a deployment slot. |
| `WebApps_ListTriggeredWebJobHistorySlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for List a triggered web job's history for an app, or a deployment slot. |
| `WebApps_ListTriggeredWebJobs` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List triggered web jobs for an app, or a deployment slot. |
| `WebApps_ListTriggeredWebJobsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for List triggered web jobs for an app, or a deployment slot. |
| `WebApps_ListUsages` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the quota usage information of an app (or deployment slot, if specified). |
| `WebApps_ListUsagesSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the quota usage information of an app (or deployment slot, if specified). |
| `WebApps_ListVnetConnections` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the virtual networks the app (or deployment slot) is connected to. |
| `WebApps_ListVnetConnectionsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Gets the virtual networks the app (or deployment slot) is connected to. |
| `WebApps_ListWebJobs` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for List webjobs for an app, or a deployment slot. |
| `WebApps_ListWebJobsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for List webjobs for an app, or a deployment slot. |
| `WebApps_MigrateMySql` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Migrates a local (in-app) MySql database to a remote MySql database. |
| `WebApps_MigrateStorage` | `EXEC` | `name, resourceGroupName, subscriptionId, subscriptionName` | Description for Restores a web app. |
| `WebApps_PutPrivateAccessVnet` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site. |
| `WebApps_PutPrivateAccessVnetSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Sets data around private site access enablement and authorized Virtual Networks that can access the site. |
| `WebApps_RecoverSiteConfigurationSnapshot` | `EXEC` | `name, resourceGroupName, snapshotId, subscriptionId` | Description for Reverts the configuration of an app to a previous snapshot. |
| `WebApps_RecoverSiteConfigurationSnapshotSlot` | `EXEC` | `name, resourceGroupName, slot, snapshotId, subscriptionId` | Description for Reverts the configuration of an app to a previous snapshot. |
| `WebApps_ResetProductionSlotConfig` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. |
| `WebApps_ResetSlotConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Resets the configuration settings of the current slot if they were previously modified by calling the API with POST. |
| `WebApps_Restart` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restarts an app (or deployment slot, if specified). |
| `WebApps_RestartSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restarts an app (or deployment slot, if specified). |
| `WebApps_Restore` | `EXEC` | `backupId, name, resourceGroupName, subscriptionId` | Description for Restores a specific backup to another app (or deployment slot, if specified). |
| `WebApps_RestoreFromBackupBlob` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restores an app from a backup blob in Azure Storage. |
| `WebApps_RestoreFromBackupBlobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restores an app from a backup blob in Azure Storage. |
| `WebApps_RestoreFromDeletedApp` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restores a deleted web app to this web app. |
| `WebApps_RestoreFromDeletedAppSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restores a deleted web app to this web app. |
| `WebApps_RestoreSlot` | `EXEC` | `backupId, name, resourceGroupName, slot, subscriptionId` | Description for Restores a specific backup to another app (or deployment slot, if specified). |
| `WebApps_RestoreSnapshot` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Restores a web app from a snapshot. |
| `WebApps_RestoreSnapshotSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Restores a web app from a snapshot. |
| `WebApps_RunTriggeredWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Run a triggered web job for an app, or a deployment slot. |
| `WebApps_RunTriggeredWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Run a triggered web job for an app, or a deployment slot. |
| `WebApps_Start` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Starts an app (or deployment slot, if specified). |
| `WebApps_StartContinuousWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Start a continuous web job for an app, or a deployment slot. |
| `WebApps_StartContinuousWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Start a continuous web job for an app, or a deployment slot. |
| `WebApps_StartNetworkTrace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Start capturing network packets for the site. |
| `WebApps_StartNetworkTraceSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Start capturing network packets for the site. |
| `WebApps_StartSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Starts an app (or deployment slot, if specified). |
| `WebApps_StartWebSiteNetworkTrace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Start capturing network packets for the site (To be deprecated). |
| `WebApps_StartWebSiteNetworkTraceOperation` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Start capturing network packets for the site. |
| `WebApps_StartWebSiteNetworkTraceOperationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Start capturing network packets for the site. |
| `WebApps_StartWebSiteNetworkTraceSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Start capturing network packets for the site (To be deprecated). |
| `WebApps_Stop` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Stops an app (or deployment slot, if specified). |
| `WebApps_StopContinuousWebJob` | `EXEC` | `name, resourceGroupName, subscriptionId, webJobName` | Description for Stop a continuous web job for an app, or a deployment slot. |
| `WebApps_StopContinuousWebJobSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, webJobName` | Description for Stop a continuous web job for an app, or a deployment slot. |
| `WebApps_StopNetworkTrace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `WebApps_StopNetworkTraceSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `WebApps_StopSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Stops an app (or deployment slot, if specified). |
| `WebApps_StopWebSiteNetworkTrace` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `WebApps_StopWebSiteNetworkTraceSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Stop ongoing capturing network packets for the site. |
| `WebApps_SwapSlotSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Swaps two deployment slots of an app. |
| `WebApps_SwapSlotWithProduction` | `EXEC` | `name, resourceGroupName, subscriptionId, data__preserveVnet, data__targetSlot` | Description for Swaps two deployment slots of an app. |
| `WebApps_SyncFunctionTriggers` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `WebApps_SyncFunctionTriggersSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `WebApps_SyncFunctions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `WebApps_SyncFunctionsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Syncs function trigger metadata to the management database |
| `WebApps_SyncRepository` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Sync web app repository. |
| `WebApps_SyncRepositorySlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Sync web app repository. |
| `WebApps_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| `WebApps_UpdateApplicationSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Replaces the application settings of an app. |
| `WebApps_UpdateApplicationSettingsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Replaces the application settings of an app. |
| `WebApps_UpdateAuthSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the Authentication / Authorization settings associated with web app. |
| `WebApps_UpdateAuthSettingsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the Authentication / Authorization settings associated with web app. |
| `WebApps_UpdateAuthSettingsV2` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates site's Authentication / Authorization settings for apps via the V2 format |
| `WebApps_UpdateAuthSettingsV2Slot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates site's Authentication / Authorization settings for apps via the V2 format |
| `WebApps_UpdateAzureStorageAccounts` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the Azure storage account configurations of an app. |
| `WebApps_UpdateAzureStorageAccountsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the Azure storage account configurations of an app. |
| `WebApps_UpdateBackupConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the backup configuration of an app. |
| `WebApps_UpdateBackupConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the backup configuration of an app. |
| `WebApps_UpdateConfiguration` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the configuration of an app. |
| `WebApps_UpdateConfigurationSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the configuration of an app. |
| `WebApps_UpdateConnectionStrings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Replaces the connection strings of an app. |
| `WebApps_UpdateConnectionStringsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Replaces the connection strings of an app. |
| `WebApps_UpdateDiagnosticLogsConfig` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the logging configuration of an app. |
| `WebApps_UpdateDiagnosticLogsConfigSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the logging configuration of an app. |
| `WebApps_UpdateDomainOwnershipIdentifier` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId` | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |
| `WebApps_UpdateDomainOwnershipIdentifierSlot` | `EXEC` | `domainOwnershipIdentifierName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |
| `WebApps_UpdateFtpAllowed` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates whether FTP is allowed on the site or not. |
| `WebApps_UpdateFtpAllowedSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates whether FTP is allowed on the site or not. |
| `WebApps_UpdateHybridConnection` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, subscriptionId` | Description for Creates a new Hybrid Connection using a Service Bus relay. |
| `WebApps_UpdateHybridConnectionSlot` | `EXEC` | `name, namespaceName, relayName, resourceGroupName, slot, subscriptionId` | Description for Creates a new Hybrid Connection using a Service Bus relay. |
| `WebApps_UpdateMetadata` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Replaces the metadata of an app. |
| `WebApps_UpdateMetadataSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Replaces the metadata of an app. |
| `WebApps_UpdatePremierAddOn` | `EXEC` | `name, premierAddOnName, resourceGroupName, subscriptionId` | Description for Updates a named add-on of an app. |
| `WebApps_UpdatePremierAddOnSlot` | `EXEC` | `name, premierAddOnName, resourceGroupName, slot, subscriptionId` | Description for Updates a named add-on of an app. |
| `WebApps_UpdateRelayServiceConnection` | `EXEC` | `entityName, name, resourceGroupName, subscriptionId` | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |
| `WebApps_UpdateRelayServiceConnectionSlot` | `EXEC` | `entityName, name, resourceGroupName, slot, subscriptionId` | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |
| `WebApps_UpdateScmAllowed` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates whether user publishing credentials are allowed on the site or not. |
| `WebApps_UpdateScmAllowedSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates whether user publishing credentials are allowed on the site or not. |
| `WebApps_UpdateSitePushSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the Push settings associated with web app. |
| `WebApps_UpdateSitePushSettingsSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the Push settings associated with web app. |
| `WebApps_UpdateSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Creates a new web, mobile, or API app in an existing resource group, or updates an existing app. |
| `WebApps_UpdateSlotConfigurationNames` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the names of application settings and connection string that remain with the slot during swap operation. |
| `WebApps_UpdateSourceControl` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Updates the source control configuration of an app. |
| `WebApps_UpdateSourceControlSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Updates the source control configuration of an app. |
| `WebApps_UpdateSwiftVirtualNetworkConnectionWithCheck` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not<br />in use by another App Service Plan other than the one this App is in. |
| `WebApps_UpdateSwiftVirtualNetworkConnectionWithCheckSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` | Description for Integrates this Web App with a Virtual Network. This requires that 1) "swiftSupported" is true when doing a GET against this resource, and 2) that the target Subnet has already been delegated, and is not<br />in use by another App Service Plan other than the one this App is in. |
| `WebApps_UpdateVnetConnection` | `EXEC` | `name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |
| `WebApps_UpdateVnetConnectionGateway` | `EXEC` | `gatewayName, name, resourceGroupName, subscriptionId, vnetName` | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
| `WebApps_UpdateVnetConnectionGatewaySlot` | `EXEC` | `gatewayName, name, resourceGroupName, slot, subscriptionId, vnetName` | Description for Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH). |
| `WebApps_UpdateVnetConnectionSlot` | `EXEC` | `name, resourceGroupName, slot, subscriptionId, vnetName` | Description for Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH). |

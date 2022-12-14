---
title: static_sites
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites
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
<tr><td><b>Name</b></td><td><code>static_sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.static_sites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `tags` | `object` | Resource tags. |
| `properties` | `object` | A static site. |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
| `sku` | `object` | Description of a SKU for a scalable resource. |
| `identity` | `object` | Managed service identity. |
| `location` | `string` | Resource Location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StaticSites_List` | `SELECT` | `subscriptionId` | Description for Get all Static Sites for a subscription. |
| `StaticSites_ApproveOrRejectPrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Approves or rejects a private endpoint connection |
| `StaticSites_CreateOrUpdateStaticSite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates a new static site in an existing resource group, or updates an existing static site. |
| `StaticSites_CreateOrUpdateStaticSiteAppSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates the app settings of a static site. |
| `StaticSites_CreateOrUpdateStaticSiteBuildAppSettings` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Creates or updates the app settings of a static site build. |
| `StaticSites_CreateOrUpdateStaticSiteBuildFunctionAppSettings` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Creates or updates the function app settings of a static site build. |
| `StaticSites_CreateOrUpdateStaticSiteCustomDomain` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Creates a new static site custom domain in an existing resource group and static site. |
| `StaticSites_CreateOrUpdateStaticSiteFunctionAppSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates or updates the function app settings of a static site. |
| `StaticSites_CreateUserRolesInvitationLink` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates an invitation link for a user with the role |
| `StaticSites_CreateZipDeploymentForStaticSite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Deploys zipped content to a static site. |
| `StaticSites_CreateZipDeploymentForStaticSiteBuild` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Deploys zipped content to a specific environment of a static site. |
| `StaticSites_DeletePrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Deletes a private endpoint connection |
| `StaticSites_DeleteStaticSite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Deletes a static site. |
| `StaticSites_DeleteStaticSiteBuild` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Deletes a static site build. |
| `StaticSites_DeleteStaticSiteCustomDomain` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Deletes a custom domain. |
| `StaticSites_DeleteStaticSiteUser` | `EXEC` | `authprovider, name, resourceGroupName, subscriptionId, userid` | Description for Deletes the user entry from the static site. |
| `StaticSites_DetachStaticSite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Detaches a static site. |
| `StaticSites_DetachUserProvidedFunctionAppFromStaticSite` | `EXEC` | `functionAppName, name, resourceGroupName, subscriptionId` | Description for Detach the user provided function app from the static site |
| `StaticSites_DetachUserProvidedFunctionAppFromStaticSiteBuild` | `EXEC` | `environmentName, functionAppName, name, resourceGroupName, subscriptionId` | Description for Detach the user provided function app from the static site build |
| `StaticSites_GetLinkedBackend` | `EXEC` | `linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_GetLinkedBackendForBuild` | `EXEC` | `environmentName, linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_GetLinkedBackends` | `EXEC` | `name, resourceGroupName, subscriptionId` |  |
| `StaticSites_GetLinkedBackendsForBuild` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_GetPrivateEndpointConnection` | `EXEC` | `name, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Description for Gets a private endpoint connection |
| `StaticSites_GetPrivateEndpointConnectionList` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the list of private endpoint connections associated with a static site |
| `StaticSites_GetPrivateLinkResources` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the private link resources |
| `StaticSites_GetStaticSite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the details of a static site. |
| `StaticSites_GetStaticSiteBuild` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Gets the details of a static site build. |
| `StaticSites_GetStaticSiteBuilds` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets all static site builds for a particular static site. |
| `StaticSites_GetStaticSiteCustomDomain` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Gets an existing custom domain for a particular static site. |
| `StaticSites_GetStaticSitesByResourceGroup` | `EXEC` | `resourceGroupName, subscriptionId` | Description for Gets all static sites in the specified resource group. |
| `StaticSites_GetUserProvidedFunctionAppForStaticSite` | `EXEC` | `functionAppName, name, resourceGroupName, subscriptionId` | Description for Gets the details of the user provided function app registered with a static site |
| `StaticSites_GetUserProvidedFunctionAppForStaticSiteBuild` | `EXEC` | `environmentName, functionAppName, name, resourceGroupName, subscriptionId` | Description for Gets the details of the user provided function app registered with a static site build |
| `StaticSites_GetUserProvidedFunctionAppsForStaticSite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the details of the user provided function apps registered with a static site |
| `StaticSites_GetUserProvidedFunctionAppsForStaticSiteBuild` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Gets the details of the user provided function apps registered with a static site build |
| `StaticSites_LinkBackend` | `EXEC` | `linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_LinkBackendToBuild` | `EXEC` | `environmentName, linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_ListStaticSiteAppSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the application settings of a static site. |
| `StaticSites_ListStaticSiteBuildAppSettings` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Gets the application settings of a static site build. |
| `StaticSites_ListStaticSiteBuildFunctionAppSettings` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Gets the application settings of a static site build. |
| `StaticSites_ListStaticSiteBuildFunctions` | `EXEC` | `environmentName, name, resourceGroupName, subscriptionId` | Description for Gets the functions of a particular static site build. |
| `StaticSites_ListStaticSiteConfiguredRoles` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Lists the roles configured for the static site. |
| `StaticSites_ListStaticSiteCustomDomains` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets all static site custom domains for a particular static site. |
| `StaticSites_ListStaticSiteFunctionAppSettings` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the application settings of a static site. |
| `StaticSites_ListStaticSiteFunctions` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Gets the functions of a static site. |
| `StaticSites_ListStaticSiteSecrets` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Lists the secrets for an existing static site. |
| `StaticSites_ListStaticSiteUsers` | `EXEC` | `authprovider, name, resourceGroupName, subscriptionId` | Description for Gets the list of users of a static site. |
| `StaticSites_PreviewWorkflow` | `EXEC` | `location, subscriptionId` | Description for Generates a preview workflow file for the static site |
| `StaticSites_RegisterUserProvidedFunctionAppWithStaticSite` | `EXEC` | `functionAppName, name, resourceGroupName, subscriptionId` | Description for Register a user provided function app with a static site |
| `StaticSites_RegisterUserProvidedFunctionAppWithStaticSiteBuild` | `EXEC` | `environmentName, functionAppName, name, resourceGroupName, subscriptionId` | Description for Register a user provided function app with a static site build |
| `StaticSites_ResetStaticSiteApiKey` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Resets the api key for an existing static site. |
| `StaticSites_UnlinkBackend` | `EXEC` | `linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_UnlinkBackendFromBuild` | `EXEC` | `environmentName, linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_UpdateStaticSite` | `EXEC` | `name, resourceGroupName, subscriptionId` | Description for Creates a new static site in an existing resource group, or updates an existing static site. |
| `StaticSites_UpdateStaticSiteUser` | `EXEC` | `authprovider, name, resourceGroupName, subscriptionId, userid` | Description for Updates a user entry with the listed roles |
| `StaticSites_ValidateBackend` | `EXEC` | `linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_ValidateBackendForBuild` | `EXEC` | `environmentName, linkedBackendName, name, resourceGroupName, subscriptionId` |  |
| `StaticSites_ValidateCustomDomainCanBeAddedToStaticSite` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Validates a particular custom domain can be added to a static site. |

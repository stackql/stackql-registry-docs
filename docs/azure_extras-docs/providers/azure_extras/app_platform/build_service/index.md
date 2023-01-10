---
title: build_service
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service
  - app_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>build_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.build_service</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BuildService_CreateOrUpdateBuild` | `EXEC` | `buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Create or update a KPack build. |
| `BuildService_GetBuild` | `EXEC` | `buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get a KPack build. |
| `BuildService_GetBuildResult` | `EXEC` | `buildName, buildResultName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get a KPack build result. |
| `BuildService_GetBuildResultLog` | `EXEC` | `buildName, buildResultName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get a KPack build result log download URL. |
| `BuildService_GetBuildService` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get a build service resource. |
| `BuildService_GetResourceUploadUrl` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get an resource upload URL for build service, which may be artifacts or source archive. |
| `BuildService_GetSupportedBuildpack` | `EXEC` | `buildServiceName, buildpackName, resourceGroupName, serviceName, subscriptionId` | Get the supported buildpack resource. |
| `BuildService_GetSupportedStack` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, stackName, subscriptionId` | Get the supported stack resource. |
| `BuildService_ListBuildResults` | `EXEC` | `buildName, buildServiceName, resourceGroupName, serviceName, subscriptionId` | List KPack build results. |
| `BuildService_ListBuildServices` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | List build services resource. |
| `BuildService_ListBuilds` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | List KPack builds. |
| `BuildService_ListSupportedBuildpacks` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get all supported buildpacks. |
| `BuildService_ListSupportedStacks` | `EXEC` | `buildServiceName, resourceGroupName, serviceName, subscriptionId` | Get all supported stacks. |

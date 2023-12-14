---
title: configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration
  - integrations
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.integrations.configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the configuration |
| `_completedAt` | `number` | A timestamp that tells you when the configuration was installed successfully |
| `_createdAt` | `number` | A timestamp that tells you when the configuration was created |
| `_deletedAt` | `number` | A timestamp that tells you when the configuration was updated. |
| `_disabledAt` | `number` | A timestamp that tells you when the configuration was disabled. Note: Configurations can be disabled when the associated user loses access to a team. They do not function during this time until the configuration is 'transferred', meaning the associated user is changed to one with access to the team. |
| `_disabledReason` | `string` |  |
| `_id` | `string` | The unique identifier of the configuration |
| `_integrationId` | `string` | The unique identifier of the app the configuration was created for |
| `_ownerId` | `string` | The user or team ID that owns the configuration |
| `_projects` | `array` | When a configuration is limited to access certain projects, this will contain each of the project ID it is allowed to access. If it is not defined, the configuration has full access. |
| `_removedLogDrainsAt` | `number` |  |
| `_removedProjectEnvsAt` | `number` |  |
| `_removedTokensAt` | `number` |  |
| `_removedWebhooksAt` | `number` |  |
| `_scopes` | `array` | The resources that are allowed to be accessed by the configuration. |
| `_scopesQueue` | `array` |  |
| `_slug` | `string` | The slug of the integration the configuration is created for. |
| `_source` | `string` | Source defines where the configuration was installed from. It is used to analyze user engagement for integration installations in product metrics. |
| `_teamId` | `string` | When the configuration was created for a team, this will show the ID of the team. |
| `_type` | `string` |  |
| `_updatedAt` | `number` | A timestamp that tells you when the configuration was updated. |
| `_userId` | `string` | The ID of the user that created the configuration. |
| `canConfigureOpenTelemetry` | `boolean` |  |
| `completedAt` | `number` | A timestamp that tells you when the configuration was installed successfully |
| `createdAt` | `number` | A timestamp that tells you when the configuration was created |
| `deletedAt` | `number` | A timestamp that tells you when the configuration was updated. |
| `disabledAt` | `number` | A timestamp that tells you when the configuration was disabled. Note: Configurations can be disabled when the associated user loses access to a team. They do not function during this time until the configuration is 'transferred', meaning the associated user is changed to one with access to the team. |
| `disabledReason` | `string` |  |
| `integrationId` | `string` | The unique identifier of the app the configuration was created for |
| `ownerId` | `string` | The user or team ID that owns the configuration |
| `projectSelection` | `string` | A string representing the permission for projects. Possible values are `all` or `selected`. |
| `projects` | `array` | When a configuration is limited to access certain projects, this will contain each of the project ID it is allowed to access. If it is not defined, the configuration has full access. |
| `removedLogDrainsAt` | `number` |  |
| `removedProjectEnvsAt` | `number` |  |
| `removedTokensAt` | `number` |  |
| `removedWebhooksAt` | `number` |  |
| `scopes` | `array` | The resources that are allowed to be accessed by the configuration. |
| `scopesQueue` | `array` |  |
| `slug` | `string` | The slug of the integration the configuration is created for. |
| `source` | `string` | Source defines where the configuration was installed from. It is used to analyze user engagement for integration installations in product metrics. |
| `teamId` | `string` | When the configuration was created for a team, this will show the ID of the team. |
| `type` | `string` |  |
| `updatedAt` | `number` | A timestamp that tells you when the configuration was updated. |
| `userId` | `string` | The ID of the user that created the configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_configuration` | `SELECT` | `id, teamId` | Allows to retrieve a the configuration with the provided id in case it exists. The authenticated user or team must be the owner of the config in order to access it. |
| `get_configurations` | `SELECT` | `teamId, view` | Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results. |
| `delete_configuration` | `DELETE` | `id, teamId` | Allows to remove the configuration with the `id` provided in the parameters. The configuration and all of its resources will be removed. This includes Webhooks, LogDrains and Project Env variables. |

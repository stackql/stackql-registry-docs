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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.integrations.configuration" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the configuration |
| <CopyableCode code="_completedAt" /> | `number` | A timestamp that tells you when the configuration was installed successfully |
| <CopyableCode code="_createdAt" /> | `number` | A timestamp that tells you when the configuration was created |
| <CopyableCode code="_deletedAt" /> | `number` | A timestamp that tells you when the configuration was updated. |
| <CopyableCode code="_disabledAt" /> | `number` | A timestamp that tells you when the configuration was disabled. Note: Configurations can be disabled when the associated user loses access to a team. They do not function during this time until the configuration is 'transferred', meaning the associated user is changed to one with access to the team. |
| <CopyableCode code="_disabledReason" /> | `string` |  |
| <CopyableCode code="_id" /> | `string` | The unique identifier of the configuration |
| <CopyableCode code="_integrationId" /> | `string` | The unique identifier of the app the configuration was created for |
| <CopyableCode code="_ownerId" /> | `string` | The user or team ID that owns the configuration |
| <CopyableCode code="_projects" /> | `array` | When a configuration is limited to access certain projects, this will contain each of the project ID it is allowed to access. If it is not defined, the configuration has full access. |
| <CopyableCode code="_removedLogDrainsAt" /> | `number` |  |
| <CopyableCode code="_removedProjectEnvsAt" /> | `number` |  |
| <CopyableCode code="_removedTokensAt" /> | `number` |  |
| <CopyableCode code="_removedWebhooksAt" /> | `number` |  |
| <CopyableCode code="_scopes" /> | `array` | The resources that are allowed to be accessed by the configuration. |
| <CopyableCode code="_scopesQueue" /> | `array` |  |
| <CopyableCode code="_slug" /> | `string` | The slug of the integration the configuration is created for. |
| <CopyableCode code="_source" /> | `string` | Source defines where the configuration was installed from. It is used to analyze user engagement for integration installations in product metrics. |
| <CopyableCode code="_teamId" /> | `string` | When the configuration was created for a team, this will show the ID of the team. |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="_updatedAt" /> | `number` | A timestamp that tells you when the configuration was updated. |
| <CopyableCode code="_userId" /> | `string` | The ID of the user that created the configuration. |
| <CopyableCode code="canConfigureOpenTelemetry" /> | `boolean` |  |
| <CopyableCode code="completedAt" /> | `number` | A timestamp that tells you when the configuration was installed successfully |
| <CopyableCode code="createdAt" /> | `number` | A timestamp that tells you when the configuration was created |
| <CopyableCode code="deletedAt" /> | `number` | A timestamp that tells you when the configuration was updated. |
| <CopyableCode code="disabledAt" /> | `number` | A timestamp that tells you when the configuration was disabled. Note: Configurations can be disabled when the associated user loses access to a team. They do not function during this time until the configuration is 'transferred', meaning the associated user is changed to one with access to the team. |
| <CopyableCode code="disabledReason" /> | `string` |  |
| <CopyableCode code="integrationId" /> | `string` | The unique identifier of the app the configuration was created for |
| <CopyableCode code="ownerId" /> | `string` | The user or team ID that owns the configuration |
| <CopyableCode code="projectSelection" /> | `string` | A string representing the permission for projects. Possible values are `all` or `selected`. |
| <CopyableCode code="projects" /> | `array` | When a configuration is limited to access certain projects, this will contain each of the project ID it is allowed to access. If it is not defined, the configuration has full access. |
| <CopyableCode code="removedLogDrainsAt" /> | `number` |  |
| <CopyableCode code="removedProjectEnvsAt" /> | `number` |  |
| <CopyableCode code="removedTokensAt" /> | `number` |  |
| <CopyableCode code="removedWebhooksAt" /> | `number` |  |
| <CopyableCode code="scopes" /> | `array` | The resources that are allowed to be accessed by the configuration. |
| <CopyableCode code="scopesQueue" /> | `array` |  |
| <CopyableCode code="slug" /> | `string` | The slug of the integration the configuration is created for. |
| <CopyableCode code="source" /> | `string` | Source defines where the configuration was installed from. It is used to analyze user engagement for integration installations in product metrics. |
| <CopyableCode code="teamId" /> | `string` | When the configuration was created for a team, this will show the ID of the team. |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updatedAt" /> | `number` | A timestamp that tells you when the configuration was updated. |
| <CopyableCode code="userId" /> | `string` | The ID of the user that created the configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_configuration" /> | `SELECT` | <CopyableCode code="id, teamId" /> | Allows to retrieve a the configuration with the provided id in case it exists. The authenticated user or team must be the owner of the config in order to access it. |
| <CopyableCode code="get_configurations" /> | `SELECT` | <CopyableCode code="teamId, view" /> | Allows to retrieve all configurations for an authenticated integration. When the `project` view is used, configurations generated for the authorization flow will be filtered out of the results. |
| <CopyableCode code="delete_configuration" /> | `DELETE` | <CopyableCode code="id, teamId" /> | Allows to remove the configuration with the `id` provided in the parameters. The configuration and all of its resources will be removed. This includes Webhooks, LogDrains and Project Env variables. |

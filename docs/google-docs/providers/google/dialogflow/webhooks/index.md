---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
  - dialogflow
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

Creates, updates, deletes or gets an <code>webhook</code> resource or lists <code>webhooks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.webhooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`. |
| <CopyableCode code="disabled" /> | `boolean` | Indicates whether the webhook is disabled. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the webhook, unique within the agent. |
| <CopyableCode code="genericWebService" /> | `object` | Represents configuration for a generic web service. |
| <CopyableCode code="serviceDirectory" /> | `object` | Represents configuration for a [Service Directory](https://cloud.google.com/service-directory) service. |
| <CopyableCode code="timeout" /> | `string` | Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_webhooks_get" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, webhooksId" /> | Retrieves the specified webhook. |
| <CopyableCode code="projects_locations_agents_webhooks_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all webhooks in the specified agent. |
| <CopyableCode code="projects_locations_agents_webhooks_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates a webhook in the specified agent. |
| <CopyableCode code="projects_locations_agents_webhooks_delete" /> | `DELETE` | <CopyableCode code="agentsId, locationsId, projectsId, webhooksId" /> | Deletes the specified webhook. |
| <CopyableCode code="projects_locations_agents_webhooks_patch" /> | `UPDATE` | <CopyableCode code="agentsId, locationsId, projectsId, webhooksId" /> | Updates the specified webhook. |

## `SELECT` examples

Returns the list of all webhooks in the specified agent.

```sql
SELECT
name,
disabled,
displayName,
genericWebService,
serviceDirectory,
timeout
FROM google.dialogflow.webhooks
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>webhooks</code> resource.

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
INSERT INTO google.dialogflow.webhooks (
agentsId,
locationsId,
projectsId,
name,
displayName,
genericWebService,
serviceDirectory,
timeout,
disabled
)
SELECT 
'{{ agentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ genericWebService }}',
'{{ serviceDirectory }}',
'{{ timeout }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: genericWebService
        value: '{{ genericWebService }}'
      - name: serviceDirectory
        value: '{{ serviceDirectory }}'
      - name: timeout
        value: '{{ timeout }}'
      - name: disabled
        value: '{{ disabled }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a webhook only if the necessary resources are available.

```sql
UPDATE google.dialogflow.webhooks
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
genericWebService = '{{ genericWebService }}',
serviceDirectory = '{{ serviceDirectory }}',
timeout = '{{ timeout }}',
disabled = true|false
WHERE 
agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND webhooksId = '{{ webhooksId }}';
```

## `DELETE` example

Deletes the specified webhook resource.

```sql
DELETE FROM google.dialogflow.webhooks
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND webhooksId = '{{ webhooksId }}';
```

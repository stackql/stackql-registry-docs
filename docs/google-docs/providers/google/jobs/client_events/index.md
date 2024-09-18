---
title: client_events
hide_title: false
hide_table_of_contents: false
keywords:
  - client_events
  - jobs
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

Creates, updates, deletes, gets or lists a <code>client_events</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.jobs.client_events" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId, tenantsId" /> | Report events issued when end user interacts with customer's application that uses Cloud Talent Solution. You may inspect the created events in [self service tools](https://console.cloud.google.com/talent-solution/overview). [Learn more](https://cloud.google.com/talent-solution/docs/management-tools) about self service tools. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>client_events</code> resource.

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
INSERT INTO google.jobs.client_events (
projectsId,
tenantsId,
requestId,
eventId,
jobEvent,
eventNotes
)
SELECT 
'{{ projectsId }}',
'{{ tenantsId }}',
'{{ requestId }}',
'{{ eventId }}',
'{{ jobEvent }}',
'{{ eventNotes }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
requestId: string
eventId: string
createTime: string
jobEvent:
  type: string
  jobs:
    - type: string
eventNotes: string

```
</TabItem>
</Tabs>

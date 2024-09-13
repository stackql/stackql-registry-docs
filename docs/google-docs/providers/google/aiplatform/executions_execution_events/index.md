
---
title: executions_execution_events
hide_title: false
hide_table_of_contents: false
keywords:
  - executions_execution_events
  - aiplatform
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

Creates, updates, deletes or gets an <code>executions_execution_event</code> resource or lists <code>executions_execution_events</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>executions_execution_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.executions_execution_events" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_execution_events" /> | `INSERT` | <CopyableCode code="executionsId, locationsId, metadataStoresId, projectsId" /> | Adds Events to the specified Execution. An Event indicates whether an Artifact was used as an input or output for an Execution. If an Event already exists between the Execution and the Artifact, the Event is skipped. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>executions_execution_events</code> resource.

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
INSERT INTO google.aiplatform.executions_execution_events (
executionsId,
locationsId,
metadataStoresId,
projectsId,
events
)
SELECT 
'{{ executionsId }}',
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ events }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: events
        value: '{{ events }}'

```
</TabItem>
</Tabs>

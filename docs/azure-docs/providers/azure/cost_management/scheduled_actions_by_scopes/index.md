---
title: scheduled_actions_by_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_actions_by_scopes
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>scheduled_actions_by_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_actions_by_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.scheduled_actions_by_scopes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, scope" /> | Create or update a shared scheduled action within the given scope. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scheduled_actions_by_scopes</code> resource.

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
INSERT INTO azure.cost_management.scheduled_actions_by_scopes (
name,
scope,
kind,
systemData,
properties
)
SELECT 
'{{ name }}',
'{{ scope }}',
'{{ kind }}',
'{{ systemData }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: eTag
      value: string
    - name: kind
      value: []
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: displayName
          value: string
        - name: fileDestination
          value:
            - name: fileFormats
              value:
                - []
        - name: notification
          value:
            - name: to
              value:
                - string
            - name: language
              value: []
            - name: message
              value: string
            - name: regionalFormat
              value: []
            - name: subject
              value: string
        - name: notificationEmail
          value: []
        - name: schedule
          value:
            - name: frequency
              value: []
            - name: hourOfDay
              value: integer
            - name: daysOfWeek
              value:
                - []
            - name: weeksOfMonth
              value:
                - []
            - name: dayOfMonth
              value: integer
            - name: startDate
              value: string
            - name: endDate
              value: string
        - name: scope
          value: string
        - name: status
          value: []
        - name: viewId
          value: string

```
</TabItem>
</Tabs>

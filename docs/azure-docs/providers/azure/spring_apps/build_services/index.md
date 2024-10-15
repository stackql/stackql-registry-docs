---
title: build_services
hide_title: false
hide_table_of_contents: false
keywords:
  - build_services
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>build_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_services" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Create a build service resource. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>build_services</code> resource.

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
INSERT INTO azure.spring_apps.build_services (
buildServiceName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ buildServiceName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: containerRegistry
          value: string
        - name: kPackVersion
          value: string
        - name: provisioningState
          value: string
        - name: resourceRequests
          value:
            - name: cpu
              value: string
            - name: memory
              value: string

```
</TabItem>
</Tabs>

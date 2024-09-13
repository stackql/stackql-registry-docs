
---
title: region_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - region_instances
  - compute
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

Creates, updates, deletes or gets an <code>region_instance</code> resource or lists <code>region_instances</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_instances" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="bulk_insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates multiple instances in a given region. Count specifies the number of instances to create. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_instances</code> resource.

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
INSERT INTO google.compute.region_instances (
project,
region,
count,
minCount,
namePattern,
perInstanceProperties,
sourceInstanceTemplate,
instanceProperties,
locationPolicy
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ count }}',
'{{ minCount }}',
'{{ namePattern }}',
'{{ perInstanceProperties }}',
'{{ sourceInstanceTemplate }}',
'{{ instanceProperties }}',
'{{ locationPolicy }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: count
        value: '{{ count }}'
      - name: minCount
        value: '{{ minCount }}'
      - name: namePattern
        value: '{{ namePattern }}'
      - name: perInstanceProperties
        value: '{{ perInstanceProperties }}'
      - name: sourceInstanceTemplate
        value: '{{ sourceInstanceTemplate }}'
      - name: instanceProperties
        value: '{{ instanceProperties }}'
      - name: locationPolicy
        value: '{{ locationPolicy }}'

```
</TabItem>
</Tabs>

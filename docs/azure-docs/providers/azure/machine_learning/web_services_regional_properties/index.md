---
title: web_services_regional_properties
hide_title: false
hide_table_of_contents: false
keywords:
  - web_services_regional_properties
  - machine_learning
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

Creates, updates, deletes, gets or lists a <code>web_services_regional_properties</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_services_regional_properties</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.machine_learning.web_services_regional_properties" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="region, resourceGroupName, subscriptionId, webServiceName" /> | Creates an encrypted credentials parameter blob for the specified region. To get the web service from a region other than the region in which it has been created, you must first call Create Regional Web Services Properties to create a copy of the encrypted credential parameter blob in that region. You only need to do this before the first time that you get the web service in the new region. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_services_regional_properties</code> resource.

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
INSERT INTO azure.machine_learning.web_services_regional_properties (
region,
resourceGroupName,
subscriptionId,
webServiceName
)
SELECT 
'{{ region }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ webServiceName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

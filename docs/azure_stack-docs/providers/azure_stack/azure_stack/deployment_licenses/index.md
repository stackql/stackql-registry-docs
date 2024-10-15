---
title: deployment_licenses
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_licenses
  - azure_stack
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

Creates, updates, deletes, gets or lists a <code>deployment_licenses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_licenses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.deployment_licenses" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="subscriptionId" /> | Creates a license that can be used to deploy an Azure Stack device. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment_licenses</code> resource.

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
INSERT INTO azure_stack.azure_stack.deployment_licenses (
subscriptionId,
verificationVersion
)
SELECT 
'{{ subscriptionId }}',
'{{ verificationVersion }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: verificationVersion
      value: string

```
</TabItem>
</Tabs>

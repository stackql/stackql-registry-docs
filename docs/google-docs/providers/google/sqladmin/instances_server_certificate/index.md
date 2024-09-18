---
title: instances_server_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_server_certificate
  - sqladmin
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

Creates, updates, deletes, gets or lists a <code>instances_server_certificate</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_server_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sqladmin.instances_server_certificate" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_server_certificate" /> | `INSERT` | <CopyableCode code="instance, project" /> | Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA. Required to prepare for a certificate rotation. If a server certificate version was previously added but never used in a certificate rotation, this operation replaces that version. There cannot be more than one certificate version waiting to be rotated in. For instances not using CAS server CA, please use AddServerCa instead. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances_server_certificate</code> resource.

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
INSERT INTO google.sqladmin.instances_server_certificate (
instance,
project
)
SELECT 
'{{ instance }}',
'{{ project }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
{}

```
</TabItem>
</Tabs>

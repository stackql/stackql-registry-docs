---
title: virtual_machine_extension_images_types
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_extension_images_types
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_extension_images_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_extension_images_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_extension_images_types" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, publisherName, subscriptionId" /> | Gets a list of virtual machine extension image types. |

## `SELECT` examples

Gets a list of virtual machine extension image types.


```sql
SELECT

FROM azure.compute.virtual_machine_extension_images_types
WHERE location = '{{ location }}'
AND publisherName = '{{ publisherName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
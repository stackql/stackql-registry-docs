---
title: instances_guest_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_guest_attributes
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

Creates, updates, deletes or gets an <code>instances_guest_attribute</code> resource or lists <code>instances_guest_attributes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_guest_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_guest_attributes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#guestAttributes for guest attributes entry. |
| <CopyableCode code="queryPath" /> | `string` | The path to be queried. This can be the default namespace ('') or a nested namespace ('\/') or a specified key ('\/\'). |
| <CopyableCode code="queryValue" /> | `object` | Array of guest attribute namespace/key/value tuples. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for this resource. |
| <CopyableCode code="variableKey" /> | `string` | The key to search for. |
| <CopyableCode code="variableValue" /> | `string` | [Output Only] The value found for the requested key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_guest_attributes" /> | `SELECT` | <CopyableCode code="instance, project, zone" /> | Returns the specified guest attributes entry. |

## `SELECT` examples

Returns the specified guest attributes entry.

```sql
SELECT
kind,
queryPath,
queryValue,
selfLink,
variableKey,
variableValue
FROM google.compute.instances_guest_attributes
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}'; 
```

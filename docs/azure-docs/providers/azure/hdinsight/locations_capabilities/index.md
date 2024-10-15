---
title: locations_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_capabilities
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>locations_capabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.locations_capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="features" /> | `array` | The capability features. |
| <CopyableCode code="quota" /> | `object` | The regional quota capability. |
| <CopyableCode code="regions" /> | `object` | The virtual machine size compatibility features. |
| <CopyableCode code="versions" /> | `object` | The version capability. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets the capabilities for the specified location. |

## `SELECT` examples

Gets the capabilities for the specified location.


```sql
SELECT
features,
quota,
regions,
versions
FROM azure.hdinsight.locations_capabilities
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
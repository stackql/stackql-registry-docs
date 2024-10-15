---
title: capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - capabilities
  - sql
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

Creates, updates, deletes, gets or lists a <code>capabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The location name. |
| <CopyableCode code="reason" /> | `string` | The reason for the capability not being available. |
| <CopyableCode code="status" /> | `string` | The status of the capability. |
| <CopyableCode code="supportedManagedInstanceVersions" /> | `array` | The list of supported managed instance versions. |
| <CopyableCode code="supportedServerVersions" /> | `array` | The list of supported server versions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Gets the subscription capabilities available for the specified location. |

## `SELECT` examples

Gets the subscription capabilities available for the specified location.


```sql
SELECT
name,
reason,
status,
supportedManagedInstanceVersions,
supportedServerVersions
FROM azure.sql.capabilities
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
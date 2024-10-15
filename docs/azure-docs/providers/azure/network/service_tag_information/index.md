---
title: service_tag_information
hide_title: false
hide_table_of_contents: false
keywords:
  - service_tag_information
  - network
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

Creates, updates, deletes, gets or lists a <code>service_tag_information</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_tag_information</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.service_tag_information" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of service tag. |
| <CopyableCode code="name" /> | `string` | The name of service tag. |
| <CopyableCode code="properties" /> | `object` | Properties of the service tag information. |
| <CopyableCode code="serviceTagChangeNumber" /> | `string` | The iteration number of service tag object for region. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets a list of service tag information resources with pagination. |

## `SELECT` examples

Gets a list of service tag information resources with pagination.


```sql
SELECT
id,
name,
properties,
serviceTagChangeNumber
FROM azure.network.service_tag_information
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
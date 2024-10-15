---
title: tag_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_resources
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tag_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tag_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="api" /> | `object` | API contract properties for the Tag Resources. |
| <CopyableCode code="operation" /> | `object` | Operation Entity contract Properties. |
| <CopyableCode code="product" /> | `object` | Product profile. |
| <CopyableCode code="tag" /> | `object` | Contract defining the Tag property in the Tag Resource Contract |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of resources associated with tags. |

## `SELECT` examples

Lists a collection of resources associated with tags.


```sql
SELECT
api,
operation,
product,
tag
FROM azure.api_management.tag_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
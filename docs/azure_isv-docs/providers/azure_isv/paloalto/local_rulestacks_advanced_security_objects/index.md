---
title: local_rulestacks_advanced_security_objects
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks_advanced_security_objects
  - paloalto
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

Creates, updates, deletes, gets or lists a <code>local_rulestacks_advanced_security_objects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_rulestacks_advanced_security_objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.local_rulestacks_advanced_security_objects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | next link |
| <CopyableCode code="value" /> | `object` | List of custom and predefined url category |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId, type" /> | Get the list of advanced security objects |

## `SELECT` examples

Get the list of advanced security objects


```sql
SELECT
nextLink,
value
FROM azure_isv.paloalto.local_rulestacks_advanced_security_objects
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND type = '{{ type }}';
```
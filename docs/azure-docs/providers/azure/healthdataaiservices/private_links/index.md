---
title: private_links
hide_title: false
hide_table_of_contents: false
keywords:
  - private_links
  - healthdataaiservices
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

Creates, updates, deletes, gets or lists a <code>private_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.healthdataaiservices.private_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_deid_service" /> | `SELECT` | <CopyableCode code="deidServiceName, resourceGroupName, subscriptionId" /> | List private links on the given resource |

## `SELECT` examples

List private links on the given resource


```sql
SELECT
properties
FROM azure.healthdataaiservices.private_links
WHERE deidServiceName = '{{ deidServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
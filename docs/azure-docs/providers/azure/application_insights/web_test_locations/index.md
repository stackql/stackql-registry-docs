---
title: web_test_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - web_test_locations
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>web_test_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_test_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.web_test_locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="DisplayName" /> | `string` | The display name of the web test location. |
| <CopyableCode code="Tag" /> | `string` | Internally defined geographic location tag. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of web test locations available to this Application Insights component. |

## `SELECT` examples

Gets a list of web test locations available to this Application Insights component.


```sql
SELECT
DisplayName,
Tag
FROM azure.application_insights.web_test_locations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
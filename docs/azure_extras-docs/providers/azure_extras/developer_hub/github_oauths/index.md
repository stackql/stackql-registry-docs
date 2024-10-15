---
title: github_oauths
hide_title: false
hide_table_of_contents: false
keywords:
  - github_oauths
  - developer_hub
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

Creates, updates, deletes, gets or lists a <code>github_oauths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>github_oauths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.developer_hub.github_oauths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The response from List GitHubOAuth operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
properties
FROM azure_extras.developer_hub.github_oauths
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
---
title: top_level_domains_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - top_level_domains_agreements
  - app_service
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

Creates, updates, deletes, gets or lists a <code>top_level_domains_agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>top_level_domains_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.top_level_domains_agreements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agreementKey" /> | `string` | Unique identifier for the agreement. |
| <CopyableCode code="content" /> | `string` | Agreement details. |
| <CopyableCode code="title" /> | `string` | Agreement title. |
| <CopyableCode code="url" /> | `string` | URL where a copy of the agreement details is hosted. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, subscriptionId" /> | Description for Gets all legal agreements that user needs to accept before purchasing a domain. |

## `SELECT` examples

Description for Gets all legal agreements that user needs to accept before purchasing a domain.


```sql
SELECT
agreementKey,
content,
title,
url
FROM azure.app_service.top_level_domains_agreements
WHERE name = '{{ name }}'
AND subscriptionId = '{{ subscriptionId }}';
```
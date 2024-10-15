---
title: service_domain_ownership_identifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - service_domain_ownership_identifiers
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

Creates, updates, deletes, gets or lists a <code>service_domain_ownership_identifiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_domain_ownership_identifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.service_domain_ownership_identifiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domainOwnershipIdentifier" /> | `string` | The domain ownership identifier value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the custom domain ownership identifier for an API Management service. |

## `SELECT` examples

Get the custom domain ownership identifier for an API Management service.


```sql
SELECT
domainOwnershipIdentifier
FROM azure.api_management.service_domain_ownership_identifiers
WHERE subscriptionId = '{{ subscriptionId }}';
```
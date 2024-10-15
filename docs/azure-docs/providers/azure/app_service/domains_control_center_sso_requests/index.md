---
title: domains_control_center_sso_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_control_center_sso_requests
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

Creates, updates, deletes, gets or lists a <code>domains_control_center_sso_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_control_center_sso_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.domains_control_center_sso_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="postParameterKey" /> | `string` | Post parameter key. |
| <CopyableCode code="postParameterValue" /> | `string` | Post parameter value. Client should use 'application/x-www-form-urlencoded' encoding for this value. |
| <CopyableCode code="url" /> | `string` | URL where the single sign-on request is to be made. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Generate a single sign-on request for the domain management portal. |

## `SELECT` examples

Description for Generate a single sign-on request for the domain management portal.


```sql
SELECT
postParameterKey,
postParameterValue,
url
FROM azure.app_service.domains_control_center_sso_requests
WHERE subscriptionId = '{{ subscriptionId }}';
```
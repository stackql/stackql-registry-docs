---
title: custom_domain_verification_ids
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domain_verification_ids
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>custom_domain_verification_ids</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_domain_verification_ids</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.custom_domain_verification_ids" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get the verification id of a subscription used for verifying custom domains |

## `SELECT` examples

Get the verification id of a subscription used for verifying custom domains


```sql
SELECT

FROM azure.container_apps.custom_domain_verification_ids
WHERE subscriptionId = '{{ subscriptionId }}';
```
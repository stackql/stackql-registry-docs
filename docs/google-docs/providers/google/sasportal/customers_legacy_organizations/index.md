---
title: customers_legacy_organizations
hide_title: false
hide_table_of_contents: false
keywords:
  - customers_legacy_organizations
  - sasportal
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

Creates, updates, deletes, gets or lists a <code>customers_legacy_organizations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customers_legacy_organizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sasportal.customers_legacy_organizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="organizations" /> | `array` | Optional. Legacy SAS organizations. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_list_legacy_organizations" /> | `SELECT` | <CopyableCode code="" /> | Returns a list of legacy organizations. |

## `SELECT` examples

Returns a list of legacy organizations.

```sql
SELECT
organizations
FROM google.sasportal.customers_legacy_organizations
;
```


---
title: firewall_policies_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policies_associations
  - compute
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

Creates, updates, deletes or gets an <code>firewall_policies_association</code> resource or lists <code>firewall_policies_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policies_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.firewall_policies_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associations" /> | `array` | A list of associations. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of firewallPolicy associations. Always compute#FirewallPoliciesListAssociations for lists of firewallPolicy associations. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_associations" /> | `SELECT` | <CopyableCode code="" /> | Lists associations of a specified target, i.e., organization or folder. |

## `SELECT` examples

Lists associations of a specified target, i.e., organization or folder.

```sql
SELECT
associations,
kind
FROM google.compute.firewall_policies_associations
WHERE  = '{{  }}'; 
```

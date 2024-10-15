---
title: private_dns_zone_suffixes
hide_title: false
hide_table_of_contents: false
keywords:
  - private_dns_zone_suffixes
  - postgresql
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

Creates, updates, deletes, gets or lists a <code>private_dns_zone_suffixes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_dns_zone_suffixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.private_dns_zone_suffixes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="exec_get" /> | `EXEC` | <CopyableCode code="" /> | Get private DNS zone suffix in the cloud |

---
title: protected_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_resources
  - kmsinventory
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

Creates, updates, deletes or gets an <code>protected_resource</code> resource or lists <code>protected_resources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protected_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.kmsinventory.protected_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="search" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Returns metadata about the resources protected by the given Cloud KMS CryptoKey in the given Cloud organization. |

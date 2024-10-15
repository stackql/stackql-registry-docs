---
title: resource_network_sibling_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_network_sibling_sets
  - netapp
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

Creates, updates, deletes, gets or lists a <code>resource_network_sibling_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_network_sibling_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.resource_network_sibling_sets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__networkFeatures, data__networkSiblingSetId, data__networkSiblingSetStateId, data__subnetId" /> | Update the network features of the specified network sibling set. |

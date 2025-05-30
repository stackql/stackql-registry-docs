---
title: diagnostics
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics
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

Creates, updates, deletes, gets or lists a <code>diagnostics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>diagnostics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.diagnostics" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="execute_site_analysis" /> | `EXEC` | <CopyableCode code="analysisName, diagnosticCategory, resourceGroupName, siteName, subscriptionId" /> | Description for Execute Analysis |
| <CopyableCode code="execute_site_analysis_slot" /> | `EXEC` | <CopyableCode code="analysisName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId" /> | Description for Execute Analysis |
| <CopyableCode code="execute_site_detector" /> | `EXEC` | <CopyableCode code="detectorName, diagnosticCategory, resourceGroupName, siteName, subscriptionId" /> | Description for Execute Detector |
| <CopyableCode code="execute_site_detector_slot" /> | `EXEC` | <CopyableCode code="detectorName, diagnosticCategory, resourceGroupName, siteName, slot, subscriptionId" /> | Description for Execute Detector |

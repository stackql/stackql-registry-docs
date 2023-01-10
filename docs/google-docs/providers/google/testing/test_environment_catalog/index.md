---
title: test_environment_catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - test_environment_catalog
  - testing
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_environment_catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.testing.test_environment_catalog</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `iosDeviceCatalog` | `object` | The currently supported iOS devices. |
| `networkConfigurationCatalog` | `object` |  |
| `softwareCatalog` | `object` | The currently provided software environment on the devices under test. |
| `androidDeviceCatalog` | `object` | The currently supported Android devices. |
| `deviceIpBlockCatalog` | `object` | List of IP blocks used by the Firebase Test Lab |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `testEnvironmentCatalog_get` | `SELECT` | `environmentType` |

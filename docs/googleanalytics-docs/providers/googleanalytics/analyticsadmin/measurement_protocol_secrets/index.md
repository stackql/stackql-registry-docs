---
title: measurement_protocol_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - measurement_protocol_secrets
  - analyticsadmin
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>measurement_protocol_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.measurement_protocol_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of this secret. This secret may be a child of any type of stream. Format: properties/&#123;property&#125;/dataStreams/&#123;dataStream&#125;/measurementProtocolSecrets/&#123;measurementProtocolSecret&#125; |
| `displayName` | `string` | Required. Human-readable display name for this secret. |
| `secretValue` | `string` | Output only. The measurement protocol secret value. Pass this value to the api_secret field of the Measurement Protocol API when sending hits to this secret's parent property. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `properties_dataStreams_measurementProtocolSecrets_get` | `SELECT` | `dataStreamsId, measurementProtocolSecretsId, propertiesId` | Lookup for a single "GA4" MeasurementProtocolSecret. |
| `properties_dataStreams_measurementProtocolSecrets_list` | `SELECT` | `dataStreamsId, propertiesId` | Returns child MeasurementProtocolSecrets under the specified parent Property. |
| `properties_dataStreams_measurementProtocolSecrets_create` | `INSERT` | `dataStreamsId, propertiesId` | Creates a measurement protocol secret. |
| `properties_dataStreams_measurementProtocolSecrets_delete` | `DELETE` | `dataStreamsId, measurementProtocolSecretsId, propertiesId` | Deletes target MeasurementProtocolSecret. |
| `properties_dataStreams_measurementProtocolSecrets_patch` | `EXEC` | `dataStreamsId, measurementProtocolSecretsId, propertiesId` | Updates a measurement protocol secret. |

---
title: downloaded_products
hide_title: false
hide_table_of_contents: false
keywords:
  - downloaded_products
  - azure_bridge_admin
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

Creates, updates, deletes, gets or lists a <code>downloaded_products</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>downloaded_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_bridge_admin.downloaded_products" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_downloaded_products', value: 'view', },
        { label: 'downloaded_products', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="activationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_part_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="compatibility" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="gallery_item_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="gallery_package_blob_sas_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_uris" /> | `text` | field from the `properties` object |
| <CopyableCode code="legal_terms" /> | `text` | field from the `properties` object |
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="payload_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="privacy_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="productName" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_details_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="vm_extension_type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for aggregate usage. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Get a downloaded product. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="activationName, resourceGroupName, subscriptionId" /> | Get a list of downloaded products. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Creates a downloaded product. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="activationName, productName, resourceGroupName, subscriptionId" /> | Delete a downloaded product. |

## `SELECT` examples

Get a list of downloaded products.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_downloaded_products', value: 'view', },
        { label: 'downloaded_products', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
activationName,
billing_part_number,
compatibility,
display_name,
gallery_item_identity,
gallery_package_blob_sas_uri,
icon_uris,
legal_terms,
links,
location,
offer,
offer_version,
payload_length,
privacy_policy,
productName,
product_details_properties,
product_kind,
product_properties,
provisioning_state,
publisher_display_name,
publisher_identifier,
resourceGroupName,
sku,
subscriptionId,
tags,
type,
vm_extension_type
FROM azure_stack.azure_bridge_admin.vw_downloaded_products
WHERE activationName = '{{ activationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.azure_bridge_admin.downloaded_products
WHERE activationName = '{{ activationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>downloaded_products</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure_stack.azure_bridge_admin.downloaded_products (
activationName,
productName,
resourceGroupName,
subscriptionId,
properties,
id,
name,
type
)
SELECT 
'{{ activationName }}',
'{{ productName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ id }}',
'{{ name }}',
'{{ type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: vmExtensionType
          value: string
        - name: links
          value: []
        - name: legalTerms
          value: string
        - name: privacyPolicy
          value: string
        - name: provisioningState
          value: []
        - name: galleryPackageBlobSasUri
          value: string
        - name: productDetailsProperties
          value:
            - name: computeRole
              value: []
            - name: isSystemExtension
              value: boolean
            - name: sourceBlob
              value:
                - name: uri
                  value: string
            - name: supportMultipleExtensions
              value: boolean
            - name: version
              value: string
            - name: vmOsType
              value: []
            - name: vmScaleSetEnabled
              value: boolean
            - name: osDiskImage
              value:
                - name: sourceBlobSasUri
                  value: string
            - name: dataDiskImages
              value:
                - - name: lun
                    value: integer
                  - name: sourceBlobSasUri
                    value: string
        - name: displayName
          value: string
        - name: description
          value: string
        - name: publisherDisplayName
          value: string
        - name: publisherIdentifier
          value: string
        - name: offer
          value: string
        - name: offerVersion
          value: string
        - name: sku
          value: string
        - name: billingPartNumber
          value: string
        - name: galleryItemIdentity
          value: string
        - name: iconUris
          value:
            - name: hero
              value: string
            - name: large
              value: string
            - name: wide
              value: string
            - name: medium
              value: string
            - name: small
              value: string
        - name: payloadLength
          value: integer
        - name: productKind
          value: string
        - name: productProperties
          value:
            - name: version
              value: string
        - name: compatibility
          value:
            - name: isCompatible
              value: boolean
            - name: message
              value: string
            - name: description
              value: string
            - name: issues
              value:
                - []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>downloaded_products</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_bridge_admin.downloaded_products
WHERE activationName = '{{ activationName }}'
AND productName = '{{ productName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

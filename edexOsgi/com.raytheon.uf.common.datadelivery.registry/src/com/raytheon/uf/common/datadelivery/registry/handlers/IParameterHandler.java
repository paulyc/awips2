/**
 * This software was developed and / or modified by Raytheon Company,
 * pursuant to Contract DG133W-05-CQ-1067 with the US Government.
 * 
 * U.S. EXPORT CONTROLLED TECHNICAL DATA
 * This software product contains export-restricted data whose
 * export/transfer/disclosure is restricted by U.S. law. Dissemination
 * to non-U.S. persons whether in the United States or abroad requires
 * an export license or other authorization.
 * 
 * Contractor Name:        Raytheon Company
 * Contractor Address:     6825 Pine Street, Suite 340
 *                         Mail Stop B8
 *                         Omaha, NE 68106
 *                         402.291.0100
 * 
 * See the AWIPS II Master Rights File ("Master Rights File.pdf") for
 * further licensing information.
 **/
package com.raytheon.uf.common.datadelivery.registry.handlers;


import java.util.List;
import java.util.Set;

import com.raytheon.uf.common.datadelivery.registry.Parameter;
import com.raytheon.uf.common.registry.handler.IRegistryObjectHandler;
import com.raytheon.uf.common.registry.handler.RegistryHandlerException;

/**
 * {@link IRegistryObjectHandler} for {@link Parameter}.
 * 
 * <pre>
 * 
 * SOFTWARE HISTORY
 * 
 * Date         Ticket#    Engineer    Description
 * ------------ ---------- ----------- --------------------------
 * Oct 3, 2012  1241      djohnson     Initial creation
 * 
 * </pre>
 * 
 * @author djohnson
 * @version 1.0
 */
public interface IParameterHandler extends IRegistryObjectHandler<Parameter> {

    /**
     * Get a list of parameter names by the specified data types.
     * 
     * @param dataTypes
     *            the data types
     * @return the list of parameter names
     * @throws RegistryHandlerException
     *             on error
     */
    Set<String> getNamesByDataTypes(List<String> dataTypes)
            throws RegistryHandlerException;

    /**
     * Retrieve the DataLevelType descriptions.
     * 
     * @param dataTypes
     *            the data types
     * @return the descriptions
     * @throws RegistryHandlerException
     *             on error
     */
    List<String> getDataLevelTypeDescriptions(List<String> dataTypes)
            throws RegistryHandlerException;
}

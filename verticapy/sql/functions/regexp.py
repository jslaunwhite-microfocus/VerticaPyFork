"""
Copyright  (c)  2018-2024 Open Text  or  one  of its
affiliates.  Licensed  under  the   Apache  License,
Version 2.0 (the  "License"); You  may  not use this
file except in compliance with the License.

You may obtain a copy of the License at:
http://www.apache.org/licenses/LICENSE-2.0

Unless  required  by applicable  law or  agreed to in
writing, software  distributed  under the  License is
distributed on an  "AS IS" BASIS,  WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.
See the  License for the specific  language governing
permissions and limitations under the License.
"""
from verticapy._typing import SQLExpression
from verticapy._utils._sql._format import format_magic

from verticapy.core.string_sql.base import StringSQL


def regexp_count(
    expr: SQLExpression,
    pattern: SQLExpression,
    position: int = 1,
) -> StringSQL:
    """
    Returns the number of times a regular expression
    matches a string.

    Parameters
    ----------
    expr: SQLExpression
        Expression.
    pattern: SQLExpression
        The regular expression to search for within
        the string.
    position: int, optional
        The number of characters from the start  of
        the  string where the function should start
        searching for matches.

    Returns
    -------
    StringSQL
        SQL string.

    Examples
    --------
    For this example, we will use the Titanic dataset.

    .. code-block:: python

        from verticapy.datasets import load_titanic

        titanic = load_titanic()

    .. note::

        VerticaPy offers a wide range of sample
        datasets that are ideal for training
        and testing purposes. You can explore
        the full list of available datasets in
        the :ref:`api.datasets`, which provides
        detailed information on each dataset and
        how to use them effectively. These datasets
        are invaluable resources for honing your
        data analysis and machine learning skills
        within the VerticaPy environment.

    Now, let's import the VerticaPy SQL functions.

    .. code-block:: python

        import verticapy.sql.functions as vpf

    Now, let's go ahead and apply the function.

    .. code-block:: python

        titanic["has_title"] = vpf.regexp_count(
            titanic["name"],
            '([A-Za-z])+\\.',
        )
        display(titanic[["name", "has_title"]])

    .. ipython:: python
        :suppress:
        :okwarning:

        from verticapy.datasets import load_titanic
        import verticapy.sql.functions as vpf
        titanic = load_titanic()
        titanic["has_title"] = vpf.regexp_count(titanic["name"], '([A-Za-z])+\\.')
        html_file = open("SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_count.html", "w")
        html_file.write(titanic[["name", "has_title"]]._repr_html_())
        html_file.close()

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_count.html

    .. note::

        It's crucial to utilize VerticaPy SQL functions in coding, as
        they can be updated over time with new syntax. While SQL
        functions typically remain stable, they may vary across platforms
        or versions. VerticaPy effectively manages these changes, a task
        not achievable with pure SQL.

    .. seealso::

        | ``vDataFrame.``:py:meth:`~verticapy.vDataFrame.eval` : Evaluates the expression.
    """
    expr = format_magic(expr)
    pattern = format_magic(pattern)
    return StringSQL(f"REGEXP_COUNT({expr}, {pattern}, {position})", "int")


def regexp_ilike(expr: SQLExpression, pattern: SQLExpression) -> StringSQL:
    """
    Returns true if the string contains a match for
    the regular expression.

    Parameters
    ----------
    expr: SQLExpression
        Expression.
    pattern: SQLExpression
        A  string containing the regular expression
        to match against the string.

    Returns
    -------
    StringSQL
        SQL string.

    Examples
    --------
    For this example, we will use the Titanic dataset.

    .. code-block:: python

        from verticapy.datasets import load_titanic

        titanic = load_titanic()

    .. note::

        VerticaPy offers a wide range of sample
        datasets that are ideal for training
        and testing purposes. You can explore
        the full list of available datasets in
        the :ref:`api.datasets`, which provides
        detailed information on each dataset and
        how to use them effectively. These datasets
        are invaluable resources for honing your
        data analysis and machine learning skills
        within the VerticaPy environment.

    Now, let's import the VerticaPy SQL functions.

    .. code-block:: python

        import verticapy.sql.functions as vpf

    Now, let's go ahead and apply the function.

    .. code-block:: python

        titanic["has_title"] = vpf.regexp_ilike(
            titanic["name"],
            '([A-Za-z])+\\.',
        )
        display(titanic[["name", "has_title"]])

    .. ipython:: python
        :suppress:
        :okwarning:

        from verticapy.datasets import load_titanic
        import verticapy.sql.functions as vpf
        titanic = load_titanic()
        titanic["has_title"] = vpf.regexp_ilike(titanic["name"], '([A-Za-z])+\\.')
        html_file = open("SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_ilike.html", "w")
        html_file.write(titanic[["name", "has_title"]]._repr_html_())
        html_file.close()

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_ilike.html

    .. note::

        It's crucial to utilize VerticaPy SQL functions in coding, as
        they can be updated over time with new syntax. While SQL
        functions typically remain stable, they may vary across platforms
        or versions. VerticaPy effectively manages these changes, a task
        not achievable with pure SQL.

    .. seealso::

        | ``vDataFrame.``:py:meth:`~verticapy.vDataFrame.eval` : Evaluates the expression.
    """
    expr = format_magic(expr)
    pattern = format_magic(pattern)
    return StringSQL(f"REGEXP_ILIKE({expr}, {pattern})")


def regexp_instr(
    expr: SQLExpression,
    pattern: SQLExpression,
    position: int = 1,
    occurrence: int = 1,
    return_position: int = 0,
) -> StringSQL:
    """
    Returns the  starting or  ending position  in a
    string  where  a  regular  expression  matches.

    Parameters
    ----------
    expr: SQLExpression
        Expression.
    pattern: SQLExpression
        The regular  expression to search for within
        the string.
    position: int, optional
        The number  of characters from the start  of
        the string where the  function should  start
        searching for matches.
    occurrence: int, optional
        Controls which occurrence of a pattern match
        in the string to return.
    return_position: int, optional
        Sets  the  position  within  the  string  to
        return.

    Returns
    -------
    StringSQL
        SQL string.

    Examples
    --------
    For this example, we will use the Titanic dataset.

    .. code-block:: python

        from verticapy.datasets import load_titanic

        titanic = load_titanic()

    .. note::

        VerticaPy offers a wide range of sample
        datasets that are ideal for training
        and testing purposes. You can explore
        the full list of available datasets in
        the :ref:`api.datasets`, which provides
        detailed information on each dataset and
        how to use them effectively. These datasets
        are invaluable resources for honing your
        data analysis and machine learning skills
        within the VerticaPy environment.

    Now, let's import the VerticaPy SQL functions.

    .. code-block:: python

        import verticapy.sql.functions as vpf

    Now, let's go ahead and apply the function.

    .. code-block:: python

        titanic["title_start"] = vpf.regexp_instr(
            titanic["name"],
            '([A-Za-z])+\\.',
            return_position = 0,
        )
        display(titanic[["name", "title_start"]])

    .. ipython:: python
        :suppress:
        :okwarning:

        from verticapy.datasets import load_titanic
        import verticapy.sql.functions as vpf
        titanic = load_titanic()
        titanic["title_start"] = vpf.regexp_instr(titanic["name"], '([A-Za-z])+\\.', return_position = 0)
        html_file = open("SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_instr.html", "w")
        html_file.write(titanic[["name", "title_start"]]._repr_html_())
        html_file.close()

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_instr.html

    .. note::

        It's crucial to utilize VerticaPy SQL functions in coding, as
        they can be updated over time with new syntax. While SQL
        functions typically remain stable, they may vary across platforms
        or versions. VerticaPy effectively manages these changes, a task
        not achievable with pure SQL.

    .. seealso::

        | ``vDataFrame.``:py:meth:`~verticapy.vDataFrame.eval` : Evaluates the expression.
    """
    expr = format_magic(expr)
    pattern = format_magic(pattern)
    return StringSQL(
        f"REGEXP_INSTR({expr}, {pattern}, {position}, {occurrence}, {return_position})"
    )


def regexp_like(expr: SQLExpression, pattern: SQLExpression) -> StringSQL:
    """
    Returns true if the string matches the regular
    expression.

    Parameters
    ----------
    expr: SQLExpression
        Expression.
    pattern: SQLExpression
        A string containing the regular expression
        to match against the string.

    Returns
    -------
    StringSQL
        SQL string.

    Examples
    --------
    For this example, we will use the Titanic dataset.

    .. code-block:: python

        from verticapy.datasets import load_titanic

        titanic = load_titanic()

    .. note::

        VerticaPy offers a wide range of sample
        datasets that are ideal for training
        and testing purposes. You can explore
        the full list of available datasets in
        the :ref:`api.datasets`, which provides
        detailed information on each dataset and
        how to use them effectively. These datasets
        are invaluable resources for honing your
        data analysis and machine learning skills
        within the VerticaPy environment.

    Now, let's import the VerticaPy SQL functions.

    .. code-block:: python

        import verticapy.sql.functions as vpf

    Now, let's go ahead and apply the function.

    .. code-block:: python

        titanic["has_title"] = vpf.regexp_like(
            titanic["name"],
            '([A-Za-z])+\\.',
        )
        display(titanic[["name", "has_title"]])

    .. ipython:: python
        :suppress:
        :okwarning:

        from verticapy.datasets import load_titanic
        import verticapy.sql.functions as vpf
        titanic = load_titanic()
        titanic["has_title"] = vpf.regexp_like(titanic["name"], '([A-Za-z])+\\.')
        html_file = open("SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_like.html", "w")
        html_file.write(titanic[["name", "has_title"]]._repr_html_())
        html_file.close()

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_like.html

    .. note::

        It's crucial to utilize VerticaPy SQL functions in coding, as
        they can be updated over time with new syntax. While SQL
        functions typically remain stable, they may vary across platforms
        or versions. VerticaPy effectively manages these changes, a task
        not achievable with pure SQL.

    .. seealso::

        | ``vDataFrame.``:py:meth:`~verticapy.vDataFrame.eval` : Evaluates the expression.
    """
    expr = format_magic(expr)
    pattern = format_magic(pattern)
    return StringSQL(f"REGEXP_LIKE({expr}, {pattern})")


def regexp_replace(
    expr: SQLExpression,
    target: SQLExpression,
    replacement: SQLExpression,
    position: int = 1,
    occurrence: int = 1,
) -> StringSQL:
    """
    Replace all occurrences of a substring that  match
    a  regular   expression  with  another  substring.

    Parameters
    ----------
    expr: SQLExpression
        Expression.
    target: SQLExpression
        The  regular  expression to search for  within
        the string.
    replacement: SQLExpression
        The string to replace matched substrings.
    position: int, optional
        The number of characters from the start of the
        string   where  the   function  should   start
        searching for matches.
    occurrence: int, optional
        Controls  which occurrence of a pattern  match
        in the string to return.

    Returns
    -------
    StringSQL
        SQL string.

    Examples
    --------
    For this example, we will use the Titanic dataset.

    .. code-block:: python

        from verticapy.datasets import load_titanic

        titanic = load_titanic()

    .. note::

        VerticaPy offers a wide range of sample
        datasets that are ideal for training
        and testing purposes. You can explore
        the full list of available datasets in
        the :ref:`api.datasets`, which provides
        detailed information on each dataset and
        how to use them effectively. These datasets
        are invaluable resources for honing your
        data analysis and machine learning skills
        within the VerticaPy environment.

    Now, let's import the VerticaPy SQL functions.

    .. code-block:: python

        import verticapy.sql.functions as vpf

    Now, let's go ahead and apply the function.

    .. code-block:: python

        titanic["new_title"] = vpf.regexp_replace(
            titanic["name"],
            '([A-Za-z])+\\.',
            '[title here] ',
        )
        display(titanic[["name", "new_title"]])

    .. ipython:: python
        :suppress:
        :okwarning:

        from verticapy.datasets import load_titanic
        import verticapy.sql.functions as vpf
        titanic = load_titanic()
        titanic["new_title"] = vpf.regexp_replace(titanic["name"], '([A-Za-z])+\\.', '[title here] ')
        html_file = open("SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_replace.html", "w")
        html_file.write(titanic[["name", "new_title"]]._repr_html_())
        html_file.close()

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_replace.html

    .. note::

        It's crucial to utilize VerticaPy SQL functions in coding, as
        they can be updated over time with new syntax. While SQL
        functions typically remain stable, they may vary across platforms
        or versions. VerticaPy effectively manages these changes, a task
        not achievable with pure SQL.

    .. seealso::

        | ``vDataFrame.``:py:meth:`~verticapy.vDataFrame.eval` : Evaluates the expression.
    """
    expr = format_magic(expr)
    target = format_magic(target)
    replacement = format_magic(replacement)
    return StringSQL(
        f"REGEXP_REPLACE({expr}, {target}, {replacement}, {position}, {occurrence})"
    )


def regexp_substr(
    expr: SQLExpression, pattern: SQLExpression, position: int = 1, occurrence: int = 1
) -> StringSQL:
    """
    Returns the  substring  that matches a regular
    expression within a string.

    Parameters
    ----------
    expr: SQLExpression
        Expression.
    pattern: SQLExpression
        The regular expression to find a substring
        to extract.
    position: int, optional
        The number of characters from the start of
        the string where the function should start
        searching for matches.
    occurrence: int, optional
        Controls  which  occurrence  of a  pattern
        match in the string to return.

    Returns
    -------
    StringSQL
        SQL string.

    Examples
    --------
    For this example, we will use the Titanic dataset.

    .. code-block:: python

        from verticapy.datasets import load_titanic

        titanic = load_titanic()

    .. note::

        VerticaPy offers a wide range of sample
        datasets that are ideal for training
        and testing purposes. You can explore
        the full list of available datasets in
        the :ref:`api.datasets`, which provides
        detailed information on each dataset and
        how to use them effectively. These datasets
        are invaluable resources for honing your
        data analysis and machine learning skills
        within the VerticaPy environment.

    Now, let's import the VerticaPy SQL functions.

    .. code-block:: python

        import verticapy.sql.functions as vpf

    Now, let's go ahead and apply the function.

    .. code-block:: python

        titanic["title"] = vpf.regexp_substr(
            titanic["name"],
            '([A-Za-z])+\\.',
        )
        display(titanic[["name", "title"]])

    .. ipython:: python
        :suppress:
        :okwarning:

        from verticapy.datasets import load_titanic
        import verticapy.sql.functions as vpf
        titanic = load_titanic()
        titanic["title"] = vpf.regexp_substr(titanic["name"], '([A-Za-z])+\\.')
        html_file = open("SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_substr.html", "w")
        html_file.write(titanic[["name", "title"]]._repr_html_())
        html_file.close()

    .. raw:: html
        :file: SPHINX_DIRECTORY/figures/sql_functions_regexp_regexp_substr.html

    .. note::

        It's crucial to utilize VerticaPy SQL functions in coding, as
        they can be updated over time with new syntax. While SQL
        functions typically remain stable, they may vary across platforms
        or versions. VerticaPy effectively manages these changes, a task
        not achievable with pure SQL.

    .. seealso::

        | ``vDataFrame.``:py:meth:`~verticapy.vDataFrame.eval` : Evaluates the expression.
    """
    expr = format_magic(expr)
    pattern = format_magic(pattern)
    return StringSQL(f"REGEXP_SUBSTR({expr}, {pattern}, {position}, {occurrence})")
